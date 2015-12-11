from django.contrib import admin
from .models import Profil,Merkez
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

admin.site.register(Merkez)
