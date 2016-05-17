from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from hasta.models import Merkez

SAAT_CHOICES = [(r,r) for r in range(0,24)]

GOZLENEN_CHOICES = (
    ('d','Doktor'),
    ('h','Hemsire'),
    ('s','Diğer sağlık personeli'),
)

GOZLEM_ADIMI_CHOICES = (
    ('e','Evet'),
    ('h','Hayır'),
    ('b','Bilmiyorum')
)

class Gozlem(models.Model):
    created_at = models.DateField(auto_now_add=True,editable=False,verbose_name="oluşturulma tarihi")
    modified_at = models.DateField(auto_now=True,editable=False,verbose_name="değiştirilme tarihi")

    merkez = models.ForeignKey(Merkez)
    gozlem_tarihi = models.DateField(verbose_name="Gözlem tarihi",)
    gozlem_saati = models.SmallIntegerField(verbose_name="Gözlem saati",choices=SAAT_CHOICES)
    gozlem_suresi = models.SmallIntegerField(verbose_name="Gözlem süresi (dakika)", validators=[MaxValueValidator(90), MinValueValidator(5)])

    def gozlem_adimi_count(self):
        gozlem_adimi_classes = self.get_gozlem_adimi_classes()
        count = 0
        for name in gozlem_adimi_classes:
            gozlem_adimi_class = gozlem_adimi_classes[name]
            count += gozlem_adimi_class.objects.filter(gozlem = self).count()
        return count

    def get_gozlem_adimi_classes(self):
        gozlem_adimi_classes = {
            'fk': FistulKanulasyonu,
            'fdk': FistulDekanulasyonu,
            'eh': ElHijyeni,
            'kb': KateterBakimi,
            'ba': BaglamaAyirma,
        }
        return gozlem_adimi_classes

    def get_gozlem_adimi_class(self,gozlem_adimi_type):
        return self.get_gozlem_adimi_classes()[gozlem_adimi_type]


    def get_gozlem_adimlari(self,gozlem_adimi_type):
        adimlar = {}
        ObjectClass = self.get_gozlem_adimi_class(gozlem_adimi_type)

        adimlar['fields'] = ObjectClass.ordered_field_list
        field_labels = []
        for field_name in adimlar['fields']:
            field_labels.append(ObjectClass._meta.get_field(field_name).verbose_name.title())
        adimlar['labels'] = field_labels
        adimlar['objects'] = ObjectClass.objects.filter(gozlem=self).all()
        return adimlar

class AbstractGozlemAdimi(models.Model):
    gozlem = models.ForeignKey(Gozlem,editable=False)

    gozlenen = models.CharField(verbose_name="Gözlenen", choices=GOZLENEN_CHOICES,max_length=1)
    ek_yorum = models.CharField(verbose_name="Ek yorum", max_length=100, blank=True)

    def get_ordered_val_list(self):
        field_vals = []
        for field_name in self.ordered_field_list:
            if field_name == 'gozlenen':
                translator = {
                    'd': 'Doktor',
                    'h': 'Hemşire',
                    's': 'Diğer'
                }
                field_vals.append(translator[getattr(self,field_name)])
            else:
                field_vals.append(getattr(self,field_name))
        return field_vals

    class Meta:
        abstract = True

class GozlemAdimiField(models.CharField):
    def __init__(self,*args,**kwargs):
        kwargs['default']= 'b'
        kwargs['max_length'] = 1
        kwargs['choices'] = GOZLEM_ADIMI_CHOICES
        super().__init__(*args,**kwargs)


class FistulKanulasyonu(AbstractGozlemAdimi):
    ga01 = GozlemAdimiField(verbose_name='Fistül yeri su ve sabunla yıkandı')
    ga02 = GozlemAdimiField(verbose_name='El hijyeni uyguladı (personel)')
    ga03 = GozlemAdimiField(verbose_name='Temiz eldiven giydi')
    ga04 = GozlemAdimiField(verbose_name='Uygun şekilde cilt antiseptiği uyguladı')
    ga05 = GozlemAdimiField(verbose_name='Antiseptiğin kurumasını bekledi')
    ga06 = GozlemAdimiField(verbose_name='Antisepsi sonrası fistül yerine temas etmedi')
    ga07 = GozlemAdimiField(verbose_name='Fistül aseptik şekilde kanüle edildi')
    ga08 = GozlemAdimiField(verbose_name='Fistül cihaza aseptik olarak bağlandı')
    ga09 = GozlemAdimiField(verbose_name='Eldiven çıkarıldı')
    ga10 = GozlemAdimiField(verbose_name='El hijyeni uygulandı')

    ordered_field_list = ['gozlenen','ga01','ga02','ga03','ga04','ga05','ga06','ga07','ga08','ga09','ga10','ek_yorum']

class FistulDekanulasyonu(AbstractGozlemAdimi):
    ga01 = GozlemAdimiField(verbose_name='El hijyeni uyguladı')
    ga02 = GozlemAdimiField(verbose_name='Temiz eldiven giydi')
    ga03 = GozlemAdimiField(verbose_name='Cihazdan aseptik olarak ayrıldı')
    ga04 = GozlemAdimiField(verbose_name='İğneler aseptik olarak ayrıldı')
    ga05 = GozlemAdimiField(verbose_name='Fistül yerine baskı uygulamak için temiz eldiven giydi (personel veya hasta)')
    ga06 = GozlemAdimiField(verbose_name='Fistül yerine temiz gazlı bez yerleştirildi')
    ga07 = GozlemAdimiField(verbose_name='Eldiven çıkarıldı (personel)')
    ga08 = GozlemAdimiField(verbose_name='El hijyeni uygulandı (personel)')
    ga09 = GozlemAdimiField(verbose_name='Eldiveni çıkardı ve el hijyeni uyguladı (hasta)')

    ordered_field_list = ['gozlenen','ga01','ga02','ga03','ga04','ga05','ga06','ga07','ga08','ga09','ek_yorum']


class ElHijyeni(AbstractGozlemAdimi):
    ga01 = GozlemAdimiField(verbose_name='Hasta İle Temas Öncesi Yıkama')
    ga02 = GozlemAdimiField(verbose_name='Hasta İle Temas Öncesi Ovalama')
    ga03 = GozlemAdimiField(verbose_name='Aseptik İşlemler Öncesi Yıkama')
    ga04 = GozlemAdimiField(verbose_name='Aseptik İşlemler Öncesi Ovalama')
    ga05 = GozlemAdimiField(verbose_name='Vücut Sıvılarının Bulaşma Riski Sonrası Yıkama')
    ga06 = GozlemAdimiField(verbose_name='Vücut Sıvılarının Bulaşma Riski Sonrası Ovalama')
    ga07 = GozlemAdimiField(verbose_name='Hasta İle Temas Sonrası Yıkama')
    ga08 = GozlemAdimiField(verbose_name='Hasta İle Temas Sonrası Ovalama')
    ga09 = GozlemAdimiField(verbose_name='Hasta Çevresi İle Temas Sonrası Yıkama')
    ga10 = GozlemAdimiField(verbose_name='Hasta Çevresi İle Temas Sonrası Ovalama')

    ordered_field_list = ['gozlenen','ga01','ga02','ga03','ga04','ga05','ga06','ga07','ga08','ga09','ga10','ek_yorum']


class KateterBakimi(AbstractGozlemAdimi):
    ga01 = GozlemAdimiField(verbose_name='Maske taktı')
    ga02 = GozlemAdimiField(verbose_name='El hijyeni uyguladı')
    ga03 = GozlemAdimiField(verbose_name='Temiz eldiven giydi')
    ga04 = GozlemAdimiField(verbose_name='Uygun şekilde cilt antiseptiği uyguladı')
    ga05 = GozlemAdimiField(verbose_name='Antiseptiğin kurumasını bekledi')
    ga06 = GozlemAdimiField(verbose_name='Antisepsi sonrası katetere temas etmedi')
    ga07 = GozlemAdimiField(verbose_name='Antibiyotikli pomad uyguladı')
    ga08 = GozlemAdimiField(verbose_name='Pansuman aseptik şekilde kapatıldı')
    ga09 = GozlemAdimiField(verbose_name='Eldiven çıkarıldı')
    ga10 = GozlemAdimiField(verbose_name='El hijyeni uygulandı')

    ordered_field_list = ['gozlenen','ga01','ga02','ga03','ga04','ga05','ga06','ga07','ga08','ga09','ga10','ek_yorum']


class BaglamaAyirma(AbstractGozlemAdimi):
    ga01 = GozlemAdimiField(verbose_name='Maske taktı')
    ga02 = GozlemAdimiField(verbose_name='El hijyeni uyguladı')
    ga03 = GozlemAdimiField(verbose_name='Temiz eldiven giydi')
    ga04 = GozlemAdimiField(verbose_name='Kateter aseptik olarak makinadan ayrıldı/bağlandı')
    ga05 = GozlemAdimiField(verbose_name='Kateter hubu silindi')
    ga06 = GozlemAdimiField(verbose_name='Hubdaki antiseptiğin kuruması beklendi')
    ga07 = GozlemAdimiField(verbose_name='Kateter kapağı aseptik olarak takıldı(cihazdan ayırdıktan sonra)')
    ga08 = GozlemAdimiField(verbose_name='Eldiven çıkarıldı')
    ga09 = GozlemAdimiField(verbose_name='El hijyeni uygulandı')

    ordered_field_list = ['gozlenen','ga01','ga02','ga03','ga04','ga05','ga06','ga07','ga08','ga09','ek_yorum']

