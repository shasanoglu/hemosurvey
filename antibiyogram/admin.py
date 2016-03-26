from django.contrib import admin
from .models import Antibiyotik,Mikroorganizma,MikroorganizmaKategorisi
# Register your models here.

class AntibiyotikAdmin(admin.ModelAdmin):
    list_display = ('id','ad','uzun_ad',)

class MikroorganizmaAdmin(admin.ModelAdmin):
    list_display = ('id','ad','kategori',)

admin.site.register(MikroorganizmaKategorisi)
admin.site.register(Antibiyotik,AntibiyotikAdmin)
admin.site.register(Mikroorganizma,MikroorganizmaAdmin)