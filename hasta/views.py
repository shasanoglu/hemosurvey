from django.shortcuts import render,redirect
from .forms import HastaForm,KateterOlayiForm, UpdateHastaForm
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse_lazy
from .models import Hasta

def add_hasta(request):
    if request.method == 'GET':
        hastaForm = HastaForm()
        kateterOlayiForm = KateterOlayiForm(prefix='kof')
    elif request.method == 'POST':
        hastaForm = HastaForm(request.POST)
        kateterOlayiForm = KateterOlayiForm(request.POST,prefix='kof')
        if hastaForm.is_valid() and  kateterOlayiForm.is_valid():
            hasta = hastaForm.save(commit=False)
            hasta.merkez = request.user.profil.merkez
            hasta.save()
            kateterOlayi = kateterOlayiForm.save(commit=False)
            kateterOlayi.hasta = hasta
            kateterOlayi.save()
            return redirect('hasta_list')

    context = {'hastaForm':hastaForm,'kateterOlayiForm':kateterOlayiForm}
    return render(request,'hasta/add_hasta.html', context)

def view_hasta(request,**kwargs):
    hasta = Hasta.objects.get(**kwargs)
    template_name = "hasta/view_hasta.html"
    kateterOlayiForm = KateterOlayiForm(prefix='kof')

    if request.method == 'POST':
        if "command" in request.POST:
            if request.POST["command"]=="new_kateter":
                kateterOlayiForm = KateterOlayiForm(request.POST,prefix='kof')
                if kateterOlayiForm.is_valid():
                    kateterOlayi = kateterOlayiForm.save(commit=False)
                    kateterOlayi.hasta = hasta
                    kateterOlayi.save()
                    return redirect('view_hasta',pk = hasta.id)

    return render(request,template_name,{
        'hasta':hasta,
        'kateterOlayiForm':kateterOlayiForm,
    })



class EditHasta(UpdateView):
    model = Hasta
    form_class = UpdateHastaForm
    template_name = "hasta/edit_hasta.html"
    def get_success_url(self):
        return reverse_lazy("view_hasta",kwargs = {"pk":self.get_object().pk,})

def hasta_list(request):
    hastalar = request.user.profil.merkez.hasta_set.all()
    context = {'hastalar':hastalar,}
    return render(request,'hasta/hasta_list.html', context)
