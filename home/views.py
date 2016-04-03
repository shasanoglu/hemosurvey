from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from.forms import AylikVeriForm, AylikVeriHelper
from.models import AylikVeri
from crispy_forms.helper import FormHelper

def home(request):
    auth_form = AuthenticationForm()
    if request.user.is_authenticated():
        eksik_aylik_veri = request.user.profil.merkez.get_missing_aylik_veri()
    else:
        eksik_aylik_veri = None
    return render(request,"home/home.html",{"auth_form":auth_form,'eksik_aylik_veri':eksik_aylik_veri})


class ContactView(TemplateView):
    template_name = 'home/contact.html'

@login_required
def aylik_veri(request):
    merkez = request.user.profil.merkez

    AylikVeriFormSet = modelformset_factory(AylikVeri,form=AylikVeriForm,extra=0)


    if request.method=='POST':
        aylik_veri_form_set = AylikVeriFormSet(request.POST,queryset=merkez.aylikveri_set.all())
        if aylik_veri_form_set.is_valid():
            instances = aylik_veri_form_set.save(commit=False)
            for instance in instances:
                instance.isUpdated = True
                instance.save()
            return redirect('home')

    else:
        aylik_veri_form_set = AylikVeriFormSet(queryset=merkez.aylikveri_set.all())

    aylik_veri_form_set_helper = AylikVeriHelper

    return render(request,'home/aylikveri.html',{'aylik_veri_form_set':aylik_veri_form_set,'aylik_veri_form_set_helper':aylik_veri_form_set_helper})
