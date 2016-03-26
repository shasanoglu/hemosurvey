from django.shortcuts import render,redirect
from .forms import HastaForm,KateterOlayiForm, UpdateHastaForm, OlayForm, AddEtkenForm
from .models import Hasta, KateterOlayi, DiyalizOlayi
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404

@login_required
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

@login_required
def view_hasta(request,**kwargs):
    hasta = Hasta.objects.get(**kwargs)

    if not hasta.merkez == request.user.profil.merkez:
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
                    return redirect('view_hasta',pk = hasta.id)

    return render(request,template_name,{
        'hasta':hasta,
        'kateterOlayiForm':kateterOlayiForm,
    })

@login_required
def edit_hasta(request,pk):
    hasta = get_object_or_404(Hasta,pk=pk)

    if not hasta.merkez == request.user.profil.merkez:
        return HttpResponseForbidden

    if request.method == 'GET':
        form = UpdateHastaForm (instance=hasta)
    elif request.method == 'POST':
        form = UpdateHastaForm(request.POST,instance=hasta)
        if form.is_valid():
            form.save()
            return redirect('view_hasta',pk=hasta.id)

    return render(request,"hasta/edit_hasta.html",{'form':form,})

@login_required
def hasta_list(request):
    hastalar = request.user.profil.merkez.hasta_set.all()
    context = {'hastalar':hastalar,}
    return render(request,'hasta/hasta_list.html', context)

@login_required
def create_olay(request,kateter_id):
    kateter = get_object_or_404(KateterOlayi,id=kateter_id)
    hasta = kateter.hasta

    if not hasta.merkez == request.user.profil.merkez:
        return HttpResponseForbidden

    if request.method == 'GET':
        form = OlayForm()
    elif request.method == 'POST':
        form = OlayForm(request.POST)
        if form.is_valid():
            olay = form.save(commit=False)
            olay.kateter = kateter
            olay.hasta = hasta
            olay.save()
            return redirect('view_olay',olay_id=olay.id)

    return render(request,'hasta/create_olay.html',{'form':form,})

@login_required
def view_olay(request,olay_id):
    olay = get_object_or_404(DiyalizOlayi,id=olay_id)
    kateter = olay.kateter
    hasta = kateter.hasta

    if not olay.kateter.hasta.merkez == request.user.profil.merkez:
        return HttpResponseForbidden

    if request.method == 'GET':
        olay_form = OlayForm(instance=olay)
        etken_form = AddEtkenForm(queryset=olay.available_etkens())
    elif request.method == 'POST':
        olay_form = OlayForm(request.POST,instance=olay)
        etken_form = AddEtkenForm(request.POST,queryset=olay.available_etkens())

        if "etken-ekle" in request.POST:
            if etken_form.is_valid():
                mikropsToAdd = etken_form.etken_form['mikroorganizmalar']
                for mikrop in mikropsToAdd.all():
                    Etken.objects.
        else:
            pass

    return render(request,'hasta/view_olay.html',{
        'olay_form':olay_form,
        'hasta':hasta,
        'kateter':kateter,
        'etken_form':etken_form,
    })