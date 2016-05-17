from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from . import forms
from .models import Gozlem, FistulKanulasyonu
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib import messages

@login_required
def create_gozlem(request):
    if request.method == 'GET':
        gozlem_form = forms.GozlemForm()
    elif request.method == 'POST':
        gozlem_form = forms.GozlemForm(request.POST)
        if gozlem_form.is_valid():
            gozlem = gozlem_form.save(commit=False)
            gozlem.merkez = request.user.profil.merkez
            gozlem.save()
            return redirect('view_gozlem', id = gozlem.id)

    context = {
        'gozlem_form' : gozlem_form,
    }

    return render(request,'gozlem/create_gozlem.html',context)

def has_permission(user,gozlem):
    if not (user.is_superuser or user.is_staff):
        if not gozlem.merkez == user.profil.merkez:
            return False
    return True

@login_required
def view_gozlem(request,id):
    def get_gozlem_adimi_types_list(post_dict = None):
        form_dict ={
            'fk': {'form': forms.FistulKanulasyonuForm, 'title': 'Fistül Kanülasyonu'},
            'fdk': {'form': forms.FistulDekanulasyonuForm, 'title': 'Fistül Dekanülasyonu'},
            'eh': {'form': forms.ElHijyeniForm, 'title': 'Hemodiyaliz Ünitesi El Hijyeni'},
            'kb': {'form': forms.KateterBakimiForm, 'title': 'Hemodiyaliz Ünitesi Kateter Bakımı'},
            'ba': {'form': forms.BaglamaAyirmaForm, 'title': 'Kateteri Diyaliz Makinasına Bağlama/Ayırma'},
        }

        ordered_list = ['fk', 'fdk', 'eh', 'kb', 'ba']

        types = []

        for type_name in ordered_list:
            type = {'name': type_name, 'title': form_dict[type_name]['title']}
            type['adimlar'] = gozlem.get_gozlem_adimlari(type_name)
            FormClass = form_dict[type_name]['form']
            if post_dict:
                type['form'] = FormClass(post_dict, prefix = type_name)
            else:
                type['form'] = FormClass(prefix = type_name)
            types.append(type)
        return types

    gozlem = get_object_or_404(Gozlem,id=id)

    if not has_permission(request.user,gozlem):
        return HttpResponseForbidden

    collapse = None
    form_error = None

    if request.method == 'GET':
        if 'collapse' in request.GET:
            collapse = request.GET['collapse']

        gozlem_form = forms.GozlemForm(instance=gozlem)
        gozlem_adimi_types = get_gozlem_adimi_types_list()

    elif request.method == 'POST':
        gozlem_form = forms.GozlemForm(request.POST, instance=gozlem)
        gozlem_adimi_types = get_gozlem_adimi_types_list(request.POST)


        if gozlem_form.is_valid():
            gozlem_form.save()

        if 'gozlem_adimi_type' in request.POST:
            gozlem_adimi_type_name = request.POST['gozlem_adimi_type']
            collapse = gozlem_adimi_type_name
            for gozlem_adimi_type in gozlem_adimi_types:
                if gozlem_adimi_type['name'] == gozlem_adimi_type_name:
                    form = gozlem_adimi_type['form']
                    if form.is_valid():
                        instance = form.save(commit = False)
                        instance.gozlem = gozlem
                        instance.save()
                        messages.info(request,'Gözlem eklendi')
                        return redirect(reverse('view_gozlem', kwargs={'id': gozlem.id, })+'?collapse={}'.format(collapse))
                    else:
                        form_error = True
                    break
        elif 'delete_adim' in request.POST:
            gozlem_adimi_type_name, id = request.POST['delete_adim'].split('|')
            collapse = gozlem_adimi_type_name
            ObjectClass = gozlem.get_gozlem_adimi_class(gozlem_adimi_type_name)
            ObjectClass.objects.get(id=id).delete()
            messages.info(request,'Gözlem silindi')
            return redirect(reverse('view_gozlem', kwargs={'id': gozlem.id, })+'?collapse={}'.format(collapse))

    context = {
        'gozlem_form' : gozlem_form,
        'gozlem_adimi_types' : gozlem_adimi_types,
        'collapse': collapse,
        'form_errors': form_error,
    }

    return render(request,'gozlem/view_gozlem.html',context)

@login_required
def gozlem_list(request):
    gozlemler = request.user.profil.merkez.gozlem_set.all()
    context = {'gozlemler':gozlemler,}
    return render(request,'gozlem/gozlem_list.html', context)

@login_required
def delete_gozlem(request,id):
    gozlem = get_object_or_404(Gozlem,id=id)
    if request.method == 'POST':
        gozlem.delete()
        messages.info(request,'Gözlemler silindi')
        return redirect('gozlem_list')