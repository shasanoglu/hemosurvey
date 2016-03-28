from django.contrib import admin
from .models import Hasta,KateterOlayi
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

admin.site.register(Etken,EtkenAdmin)
admin.site.register(Duyarlilik)

