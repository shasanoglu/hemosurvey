from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import datetime

class Merkez(models.Model):
    def __str__(self):
        return self.isim
    isim = models.CharField(max_length=60,unique=True)

    #Calisma baslamadan bir onceki ay
    VERI_BEFORE_START_YEAR = 2016
    VERI_BEFORE_START_MONTH = 3

    def create_missing_month_data(self):
        if self.aylikveri_set.exists():
            max_year = self.aylikveri_set.all().aggregate(models.Max('yil'))['yil__max']
            max_month = self.aylikveri_set.filter(yil=max_year).aggregate(models.Max('ay'))['ay__max']
        else:
            max_year = self.VERI_BEFORE_START_YEAR
            max_month = self.VERI_BEFORE_START_MONTH

        cur_month = datetime.date.today().month
        cur_year = datetime.date.today().year

        if max_year < cur_year or max_month < cur_month:
            while not (max_month == cur_month and max_year == cur_year):
                #calc next month
                if max_month == 12:
                    max_month == 1
                    max_year = max_year + 1
                else:
                    max_month = max_month + 1

                AylikVeri.objects.create(merkez=self, ay=max_month, yil=max_year)

    def get_missing_aylik_veri(self):
        self.create_missing_month_data()
        return self.aylikveri_set.filter(isUpdated=False)

    class Meta:
        verbose_name_plural = "merkezler"

#Kullanicilarla ilgili ekstra bilgileri tuttugumuz model
class Profil(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    telefon = models.CharField(max_length=15,default="+90 ")
    merkez = models.ForeignKey(Merkez,blank=False)


# def save_user_callback(sender, instance, created, **kwargs):
#     if created:
#         Profil.objects.get_or_create(user=instance)
#
#
# post_save.connect(save_user_callback,sender=User)

class AylikVeri(models.Model):
    def __str__(self):
        return "{} {}".format(self.verbose_ay(),self.yil)
    AY_CHOICES = (
        (1,'Ocak'),
        (2,'Şubat'),
        (3,'Mart'),
        (4,'Nisan'),
        (5,'Mayıs'),
        (6,'Haziran'),
        (7,'Temmuz'),
        (8,'Ağustos'),
        (9,'Eylül'),
        (10,'Ekim'),
        (11,'Kasım'),
        (12,'Aralık'),
    )

    YIL_CHOICES = [(r,r) for r in range(2016,2020)]

    merkez = models.ForeignKey(Merkez,editable=False)
    isUpdated = models.BooleanField(editable=False,default=False)
    ay = models.PositiveSmallIntegerField('Ay',choices=AY_CHOICES,editable=False)
    yil = models.PositiveSmallIntegerField('Yıl',choices=YIL_CHOICES,editable=False)
    ilk_iki_gun = models.PositiveSmallIntegerField('Ayın ilk iki çalışma gününde merkezinizde diyalize giren hasta sayısı',default=0)

    def verbose_ay(self):
        return dict(self.AY_CHOICES)[self.ay]



