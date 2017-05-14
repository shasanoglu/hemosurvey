from django.db import models
from home.models import Merkez
import datetime
from localflavor.tr.tr_provinces import PROVINCE_CHOICES
from antibiyogram.models import Mikroorganizma,Antibiyotik
from django.core.exceptions import ObjectDoesNotExist

class Hasta(models.Model):
    def __str__(self):
        return str(self.tckn)

    merkez = models.ForeignKey(Merkez)
    created_at = models.DateField(auto_now_add=True,editable=False,verbose_name="oluşturulma tarihi")
    modified_at = models.DateField(auto_now=True,editable=False,verbose_name="değiştirilme tarihi")
    tckn = models.BigIntegerField(unique=False,verbose_name="Dosya No")
    ad = models.CharField(max_length=25)
    soyad = models.CharField(max_length=25)

    YEAR_CHOICES = [(r,r) for r in range(1930, datetime.date.today().year+1)]
    SEX_CHOICES = (('e','Erkek'),('k','Kadın'))
    BOY_CHOICES = [(r,r) for r in range(100,230)]
    KILO_CHOICES = [(r,r) for r in range(20,140)]
    CALISMA_CHOICES = (('e','Çalışıyor'),('h','Çalışmıyor'))

    dogum_yili = models.IntegerField(verbose_name="Doğum yılı", choices=YEAR_CHOICES, default=datetime.datetime.now().year-50)
    cinsiyet = models.CharField(verbose_name="Cinsiyet",max_length=1,choices=SEX_CHOICES,default="k")

    boy = models.IntegerField(verbose_name="Boy",choices=BOY_CHOICES,default=167, null=True, blank=True)
    kilo = models.IntegerField(verbose_name="Kilo",choices=KILO_CHOICES,default=72, null=True, blank=True)
    diyaliz_ilk_yil = models.IntegerField(verbose_name="Diyalize ilk girdiği yıl", choices=YEAR_CHOICES, default=datetime.datetime.now().year-10)
    calisma_durumu = models.CharField(verbose_name='Çalışma durumu',choices=CALISMA_CHOICES,max_length=1,default='h')
    yasadigi_il = models.CharField(verbose_name='Yaşadığı il',max_length=2,choices=PROVINCE_CHOICES,default='34')

    #Diyaliz için altta yatan hastalık
    ayh_HT = models.BooleanField(verbose_name="HT",default=False)
    ayh_DM = models.BooleanField(verbose_name="DM",default=False)
    polikistik_bobrek = models.BooleanField(verbose_name="Polikistik böbrek",default=False)
    dogustan_tek_bobrek = models.BooleanField(verbose_name="Doğuştan tek böbrek",default=False)
    ailesel_bobrek_hastaliklari = models.BooleanField(verbose_name="Ailesel böbrek hastalıkları",default=False)
    nefrolitiazis =  models.BooleanField(verbose_name="Nefrolitiazis",default=False)
    idiopatik =  models.BooleanField(verbose_name="İdiopatik",default=False)
    ayh_diger = models.BooleanField(verbose_name="Diğer",default=False)

    #Komorbid hastalık
    kh_HT = models.BooleanField(verbose_name="HT",default=False)
    kh_DM = models.BooleanField(verbose_name="DM",default=False)
    gecirilmis_SVO = models.BooleanField(verbose_name="Geçirilmiş SVO",default=False)
    koroner_arter_hastaligi = models.BooleanField(verbose_name="Koroner arter hastalığı",default=False)
    astim_koah = models.BooleanField(verbose_name="Astım/KOAH",default=False)
    kh_diger = models.BooleanField(verbose_name="Diğer",default=False)

    #Bağımlılık
    alkol = models.BooleanField(verbose_name="Alkol",default=False)
    sigara = models.BooleanField(verbose_name="Sigara",default=False)
    uyusturucu_madde = models.BooleanField(verbose_name="Uyuşturucu madde",default=False)

    #Hepatit serolojisi


    SEROLOJI_CHOICES = (('p','Pozitif'), ('n', 'Negatif'), ('b','Bakılmadı'))
    HBsAg = models.CharField(verbose_name="HBsAg",max_length=1,default='b',choices=SEROLOJI_CHOICES)
    AntiHBs = models.CharField(verbose_name="AntiHBs",max_length=1,default='b',choices=SEROLOJI_CHOICES)
    AntiHBcIgG = models.CharField(verbose_name="AntiHBcIgG",max_length=1,default='b',choices=SEROLOJI_CHOICES)
    AntiHBcIgM = models.CharField(verbose_name="AntiHBcIgM",max_length=1,default='b',choices=SEROLOJI_CHOICES)
    AntiHCV = models.CharField(verbose_name="AntiHCV",max_length=1,default='b',choices=SEROLOJI_CHOICES)
    AntiHIV = models.CharField(verbose_name="AntiHIV",max_length=1,default='b',choices=SEROLOJI_CHOICES)

    MRSA_CHOICES = (('v','Var'),('y','Yok'),('b','Bilinmiyor'))
    YES_NO_CHOICES = (('e','Evet'),('h','Hayır'),)

    #Diğer
    MRSA_kolonizayonu = models.CharField(verbose_name="MRSA kolonizasyonu",max_length=1,choices=MRSA_CHOICES,default='y')
    influenza_asisi = models.CharField(verbose_name="İnfluenza aşısı olmuş mu?",max_length=1,choices=YES_NO_CHOICES,default='h')
    pnomokok_asisi = models.CharField(verbose_name="Pnömokok aşısı olmuş mu?",max_length=1,choices=YES_NO_CHOICES,default='h')
    egitim = models.CharField(verbose_name="Hasta kateter/fistül bakımı için eğitim almış mı?",max_length=1,choices=YES_NO_CHOICES,default='h')

    class Meta:
        verbose_name_plural = "hastalar"

    def verbose_cinsiyet(self):
        return dict(self.SEX_CHOICES)[self.cinsiyet]


class KateterOlayi(models.Model):
    TIP_CHOICES = (
        ('gecici_k','Geçici kateter'),
        ('kalici_k','Kalıcı kateter'),
        ('fistul','AV Fistül'),
        ('greft','AV Greft'),
    )
    MERKEZ_CHOICES = (
        ('d','Devlet Hastanesi'),
        ('a','Araştırma Hastanesi'),
        ('u','Üniversite Hastanesi'),
        ('o','Özel Hastane')
    )
    YER_CHOICES = (
        ('s','subklavian'),
        ('j','juguler'),
        ('f','femoral')
    )
    NEDEN_CHOICES = (
        ('c','Çalışmaması'),
        ('e','Enfekte olması'),
        ('k','Kendiliğinden çıkması'),
        ('d','Diğer')
    )
    hasta = models.ForeignKey(Hasta)
    created_at = models.DateField(auto_now_add=True,editable=False,verbose_name="oluşturulma tarihi")
    modified_at = models.DateField(auto_now=True,editable=False,verbose_name="değiştirilme tarihi")

    tip = models.CharField(max_length=10,choices=TIP_CHOICES)
    takilma_tarihi = models.DateField(verbose_name="Takılma/Açılma tarihi",)
    takildigi_merkez = models.CharField(verbose_name='Takıldığı/açıldığı merkez',max_length=1,default='a',choices=MERKEZ_CHOICES)
    yeri = models.CharField(verbose_name="Yeri",max_length=1,default='s',choices=YER_CHOICES)
    degisim_nedeni = models.CharField(verbose_name='Değişim nedeni',default='d',choices=NEDEN_CHOICES,max_length=1)


    class Meta:
        verbose_name_plural = "kateter olayları"
        verbose_name = "kateter olayı"
        ordering = ['takilma_tarihi']

    def verbose_tip(self):
        return dict(self.TIP_CHOICES)[self.tip]

    def verbose_yeri(self):
        s = ''
        if not self.tip == 'fistul':
            s = dict(self.YER_CHOICES)[self.yeri]
        return s

    def verbose_degisim_nedeni(self):
        s = ''
        if not self.tip == 'fistul':
            s = dict(self.NEDEN_CHOICES)[self.degisim_nedeni]
        return s

    def verbose_takildigi_merkez(self):
        return dict(self.MERKEZ_CHOICES)[self.takildigi_merkez]



class DiyalizOlayi(models.Model):
    kateter = models.ForeignKey(KateterOlayi)
    hasta = models.ForeignKey(Hasta)

    created_at = models.DateField(auto_now_add=True,editable=False,verbose_name="oluşturulma tarihi")
    modified_at = models.DateField(auto_now=True,editable=False,verbose_name="değiştirilme tarihi")

    olay_tarihi = models.DateField(verbose_name="Olay tarihi")

    isi_hiperemi_puy = models.BooleanField(verbose_name='FİSTÜL/KATETER BÖLGESİNSE ISI ARTIŞI/HİPEREMİ/PÜY VARLIĞI',default=False)
    iv_antibiyotik = models.BooleanField(verbose_name="IV ANTİBİYOTİK TEDAVİSİ",default=False)
    kan_kulturunde_ureme = models.BooleanField(verbose_name="KAN KÜLTÜRÜNDE ÜREME",default=False)

    gecici_hasta = models.BooleanField(verbose_name="Geçici Hasta",default=False, help_text="Ünitenizin devamlı hastası değilse işaretleyiniz")

    OLASI_KAYNAK_CHOICES = (
        ('v', 'Vasküler giriş'),
        ('vh', 'Vasküler giriş harici'),
        ('k', 'Kontaminasyon'),
        ('b', 'Belirsiz'),
    )
    ETKEN_ALINDI_MI_CHOICES = (
        ('e', 'Evet'),
        ('h', 'Hayır')
    )

    #Kan kulturunde ureme ile ilgili
    kateterde_ureme = models.BooleanField(verbose_name="Kateterde üreme",default=False)
    periferde_ureme = models.BooleanField(verbose_name="Periferde üreme",default=False)
    etken_alindi_mi = models.CharField(verbose_name="Etken alındı mı?",max_length=1,default='h',choices=ETKEN_ALINDI_MI_CHOICES)
    olasi_kaynak = models.CharField(verbose_name="Pozitif kan kültürünün olası kaynağı",max_length=2,default='b',choices=OLASI_KAYNAK_CHOICES)

    #spesifik problemler
    ates = models.BooleanField(verbose_name="Ateş",default=False)
    hipotansiyon = models.BooleanField(verbose_name="Hipotansiyon (TA< 120/80)",default=False)
    acik_yara = models.BooleanField(verbose_name="Kateter / Fistül girişi dışında bir bölgede açık yara",default=False)
    selulit = models.BooleanField(verbose_name="Kateter/Fistül girişi dışında bir bölgede selülit",default=False)
    uriner_enfeksiyon = models.BooleanField(verbose_name="Üriner enfeksiyon",default=False)
    pnomoni_sye = models.BooleanField(verbose_name="Pnömoni/ solunum yolu enfeksiyonu",default=False)
    diger = models.BooleanField(verbose_name="Diğer",default=False)

    GELISEN_CHOICES = (
        ('e', 'Evet'),
        ('h', 'Hayır'),
        ('b', 'Bilinmiyor'),
    )

    #OLAYA BAĞLI GELİŞEN MORTALİTE/MORBİDİTE
    kateter_cikarildi = models.CharField(verbose_name="Kateter çıkarıldı",max_length=1,default='b',choices=GELISEN_CHOICES)
    hospitalizasyon = models.CharField(verbose_name="Hospitalizasyon",max_length=1,default='b',choices=GELISEN_CHOICES)
    olum = models.CharField(verbose_name="Ölüm",max_length=1,default='b',choices=GELISEN_CHOICES)


    def available_etkens(self):
        return Mikroorganizma.objects.exclude(etken__olay=self).order_by('kategori','ad')

    class Meta:
        ordering = ['olay_tarihi']

class Etken(models.Model):
    olay = models.ForeignKey(DiyalizOlayi)
    mikroorganizma = models.ForeignKey(Mikroorganizma)

    def get_duyarliliklar(self):
        duyarliliklar = []
        for antibiyotik in self.mikroorganizma.antibiyotikler.all():
            try:
                duyarlilik = self.duyarlilik_set.get(antibiyotik=antibiyotik)
            except ObjectDoesNotExist:
                duyarlilik = Duyarlilik.objects.create(antibiyotik=antibiyotik,etken=self)
            duyarliliklar.append(duyarlilik)
        return duyarliliklar



DIRENC_CHOICES = (
    ('','Bakılmadı'),
    ('d','Duyarli'),
    ('o','Orta Duyarlı'),
    ('r','Dirençli'),
)

class Duyarlilik(models.Model):
    etken = models.ForeignKey(Etken)
    antibiyotik = models.ForeignKey(Antibiyotik)
    direnc = models.CharField(verbose_name='Direnç',max_length=1,blank=True,choices=DIRENC_CHOICES)

