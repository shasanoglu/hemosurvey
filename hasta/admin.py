from django.contrib import admin
from .models import Hasta,KateterOlayi,DiyalizOlayi
from .models import Etken,Duyarlilik

class KateterOlayiInline(admin.StackedInline):
    model = KateterOlayi
    can_delete = False

class HastaAdmin(admin.ModelAdmin):
    list_display = ('id','tckn','ad','soyad',)
    inlines = [KateterOlayiInline,]

admin.site.register(Hasta,HastaAdmin)

class DuyarlilikInline(admin.TabularInline):
    model = Duyarlilik

class EtkenAdmin(admin.ModelAdmin):
    list_display = ('id','mikroorganizma')
    inlines = [DuyarlilikInline,]

class OlayAdmin(admin.ModelAdmin):
    list_display = ('id','hasta','kateter','olay_tarihi',)

admin.site.register(Etken,EtkenAdmin)
admin.site.register(Duyarlilik)
admin.site.register(DiyalizOlayi,OlayAdmin)

