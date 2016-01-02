from django.db import models
from home.models import Merkez

class Hasta(models.Model):
    def __str__(self):
        return str(self.tckn)

    merkez = models.ForeignKey(Merkez)
    created_at = models.DateField(auto_now_add=True,editable=False,verbose_name="oluşturulma tarihi")
    modified_at = models.DateField(auto_now=True,editable=False,verbose_name="değiştirilme tarihi")
    tckn = models.BigIntegerField(unique=True,verbose_name="TC Kimlik No")
    ad = models.CharField(max_length=25)
    soyad = models.CharField(max_length=25)
    class Meta:
        verbose_name_plural = "hastalar"


class KateterOlayi(models.Model):
    TIP_CHOICES = (
        ('gecici','Geçici'),
        ('kalici','Kalıcı')
    )
    hasta = models.ForeignKey(Hasta)
    created_at = models.DateField(auto_now_add=True,editable=False,verbose_name="oluşturulma tarihi")
    modified_at = models.DateField(auto_now=True,editable=False,verbose_name="değiştirilme tarihi")
    takilma_tarihi = models.DateField(verbose_name="takılma tarihi",)
    tip = models.CharField(max_length=10,choices=TIP_CHOICES)

    class Meta:
        verbose_name_plural = "kateter olayları"
        verbose_name = "kateter olayı"