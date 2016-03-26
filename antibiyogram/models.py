from django.db import models

class MikroorganizmaKategorisi(models.Model):
    def __str__(self):
        return self.ad

    ad = models.CharField(max_length=30,unique=True)

class Antibiyotik(models.Model):
    def __str__(self):
        return self.uzun_ad

    ad = models.CharField(max_length=10,unique=True)
    uzun_ad = models.CharField(max_length=30)

class Mikroorganizma(models.Model):
    def __str__(self):
        return '{} | {}'.format(self.kategori.ad, self.ad)

    ad = models.CharField(max_length=60,unique=True)
    kategori = models.ForeignKey(MikroorganizmaKategorisi)
    antibiyotikler = models.ManyToManyField(Antibiyotik)
