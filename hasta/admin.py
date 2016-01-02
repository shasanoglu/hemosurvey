from django.contrib import admin
from .models import Hasta,KateterOlayi

class KateterOlayiInline(admin.StackedInline):
    model = KateterOlayi
    can_delete = False

class HastaAdmin(admin.ModelAdmin):
    list_display = ('id','tckn','ad','soyad',)
    inlines = [KateterOlayiInline,]

admin.site.register(Hasta,HastaAdmin)
