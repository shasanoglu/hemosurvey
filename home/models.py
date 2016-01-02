from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Merkez(models.Model):
    def __str__(self):
        return self.isim
    isim = models.CharField(max_length=60,unique=True)

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

