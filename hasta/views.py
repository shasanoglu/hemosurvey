from django.shortcuts import render, redirect
from .forms import HastaForm,KateterOlayiForm, UpdateHastaForm, OlayForm, AddEtkenForm, DuyarlilikForm
from .models import Hasta, KateterOlayi, DiyalizOlayi, Etken
from antibiyogram.models import Mikroorganizma
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404
from django.contrib import messages

@login_required
def add_hasta(request):
    if request.method == 'GET':
        hastaForm = HastaForm()
        kateterOlayiForm = KateterOlayiForm(prefix='kof',hidden_neden=True)
    elif request.method == 'POST':
        hastaForm = HastaForm(request.POST, merkez=request.user.profil.merkez)
        kateterOlayiForm = KateterOlayiForm(request.POST,prefix='kof',hidden_neden=True)
        if hastaForm.is_valid() and  kateterOlayiForm.is_valid():
            hasta = hastaForm.save(commit=False)
            hasta.merkez = request.user.profil.merkez
            hasta.save()
            kateterOlayi = kateterOlayiForm.save(commit=False)
            kateterOlayi.hasta = hasta
            kateterOlayi.save()
            messages.info(request,'Hasta oluşturuldu')
            return redirect('view_hasta',pk = hasta.id)

    context = {'hastaForm':hastaForm,'kateterOlayiForm':kateterOlayiForm}
    return render(request,'hasta/add_hasta.html', context)

def has_permission(user,hasta):
    if not (user.is_superuser or user.is_staff):
        if not hasta.merkez == user.profil.merkez:
            return False
    return True

@login_required
def view_hasta(request,**kwargs):
    hasta = Hasta.objects.get(**kwargs)

    if not has_permission(request.user,hasta):
        return HttpResponseForbidden

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
                    messages.info(request,'{} eklendi'.format(kateterOlayi.verbose_tip()))
                    return redirect('view_hasta',pk = hasta.id)

    return render(request,template_name,{
        'hasta':hasta,
        'kateterOlayiForm':kateterOlayiForm,
    })

@login_required
def edit_hasta(request,pk):
    hasta = get_object_or_404(Hasta,pk=pk)

    if not has_permission(request.user,hasta):
        return HttpResponseForbidden

    if request.method == 'GET':
        form = UpdateHastaForm (instance=hasta)
    elif request.method == 'POST':
        form = UpdateHastaForm(request.POST,instance=hasta, merkez=request.user.profil.merkez)
        if form.is_valid():
            form.save()
            messages.info(request,'Hasta bilgileri güncellendi')
            return redirect('view_hasta',pk=hasta.id)

    return render(request,"hasta/edit_hasta.html",{'form':form,})

@login_required
def hasta_list(request):
    hastalar = request.user.profil.merkez.hasta_set.all()
    context = {'hastalar':hastalar,}
    return render(request,'hasta/hasta_list.html', context)

@login_required
def hasta_list_all(request):
    hastalar = Hasta.objects.all()
    context = {'hastalar':hastalar,'merkez_column':True}
    return render(request,'hasta/hasta_list.html', context)

@login_required
def create_olay(request,kateter_id):
    kateter = get_object_or_404(KateterOlayi,id=kateter_id)
    hasta = kateter.hasta

    if not has_permission(request.user,hasta):
        return HttpResponseForbidden

    if request.method == 'GET':
        form = OlayForm()
    elif request.method == 'POST':
        form = OlayForm(request.POST,hasta=hasta)
        if form.is_valid():
            olay = form.save(commit=False)
            olay.kateter = kateter
            olay.hasta = hasta
            olay.save()
            messages.info(request,'Diyaliz ilişkili olay eklendi')
            return redirect('view_olay',olay_id=olay.id)

    return render(request,'hasta/create_olay.html',{'form':form,})

@login_required
def view_olay(request,olay_id):
    def get_etkenler():
        etkenler = []
        for etken in olay.etken_set.all():
            duyarlilik_forms = []
            for duyarlilik in etken.get_duyarliliklar():
                if request.method == 'GET':
                    duyarlilik_forms.append(DuyarlilikForm(instance=duyarlilik,
                                                           direnc_label_name=duyarlilik.antibiyotik.uzun_ad,
                                                           prefix='d-{}'.format(duyarlilik.id)))
                elif request.method == 'POST':
                    duyarlilik_forms.append(DuyarlilikForm(request.POST,
                                                           instance=duyarlilik,
                                                           direnc_label_name=duyarlilik.antibiyotik.uzun_ad,
                                                           prefix='d-{}'.format(duyarlilik.id)))
            etkenler.append({
                'instance': etken,
                'duyarlilik_forms': duyarlilik_forms,
            })
        return etkenler


    olay = get_object_or_404(DiyalizOlayi,id=olay_id)
    kateter = olay.kateter
    hasta = kateter.hasta

    if not has_permission(request.user,hasta):
        return HttpResponseForbidden

    if request.method == 'GET':
        olay_form = OlayForm(instance=olay)
        etken_form = AddEtkenForm(queryset=olay.available_etkens())
        etkenler = get_etkenler()
    elif request.method == 'POST':
        olay_form = OlayForm(request.POST,instance=olay)
        etken_form = AddEtkenForm(request.POST,queryset=olay.available_etkens())

        if "etken-ekle" in request.POST:
            if etken_form.is_valid():
                mikropsToAdd = etken_form.cleaned_data['mikroorganizmalar']
                for mikrop in mikropsToAdd:
                    if not olay.etken_set.filter(mikroorganizma=mikrop).exists():
                        Etken.objects.create(olay=olay,mikroorganizma=mikrop)
                        messages.info(request,'Etken eklendi')
            etkenler = get_etkenler()
        elif "delete-etken" in request.POST:
            etken = get_object_or_404(Etken,id=request.POST["delete-etken"])
            etken.delete()
            messages.info(request,'Etken silindi')
            etkenler = get_etkenler()
        else:
            etkenler = get_etkenler()
            all_is_well = True

            if olay_form.is_valid():
                olay_form.save()
            else:
                all_is_well = False

            for etken in etkenler:
                for duyarlilik_form in etken['duyarlilik_forms']:
                    if duyarlilik_form.is_valid():
                        duyarlilik_form.save()
                    else:
                        all_is_well = False

            if all_is_well:
                messages.info(request,'Diyaliz ilişkili olay bilgileri güncellendi')
                return redirect('view_olay',olay_id=olay.id)



    return render(request,'hasta/view_olay.html',{
        'olay_form':olay_form,
        'hasta':hasta,
        'kateter':kateter,
        'olay':olay,
        'etken_form':etken_form,
        'etkenler': etkenler,
    })


@login_required
def delete_hasta(request,hasta_id):
    hasta = get_object_or_404(Hasta,id=hasta_id)
    if request.method == 'POST':
        hasta.delete()
        messages.info(request,'Hasta silindi')
        return redirect('hasta_list')


@login_required
def delete_kateter(request,kateter_id):
    kateter = get_object_or_404(KateterOlayi,id=kateter_id)
    hasta_id = kateter.hasta.id
    if request.method == 'POST':
        tip = kateter.verbose_tip()
        kateter.delete()
        messages.info(request,'{} silindi'.format(tip))
        return redirect('view_hasta',pk=hasta_id)


@login_required
def delete_olay(request,olay_id):
    olay = get_object_or_404(DiyalizOlayi,id=olay_id)
    hasta_id = olay.hasta.id
    if request.method == 'POST':
        olay.delete()
        messages.info(request,'Diyaliz ilişkili olay silindi')
        return redirect('view_hasta',pk=hasta_id)