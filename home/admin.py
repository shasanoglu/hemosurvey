from django.contrib import admin
from .models import Profil,Merkez, AylikVeri
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

class ProfilInline(admin.StackedInline):
    model = Profil
    max_num = 1
    can_delete = False

class CustomUserAdmin(UserAdmin):
    inlines = [ProfilInline]

# unregister old user admin
admin.site.unregister(User)
# register new user admin
admin.site.register(User, CustomUserAdmin)

class AylikVeriInline(admin.StackedInline):
    model = AylikVeri
    can_delete = False

class CustomMerkezAdmin(admin.ModelAdmin):
    inlines = [AylikVeriInline,]


admin.site.register(Merkez,CustomMerkezAdmin)
admin.site.register(AylikVeri)
