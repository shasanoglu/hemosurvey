from django.shortcuts import render,redirect
from .forms import HastaForm,KateterOlayiForm

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
            return redirect('home') #TASK: Change this to hastalar view

    context = {'hastaForm':hastaForm,'kateterOlayiForm':kateterOlayiForm}
    return render(request,'hasta/add_hasta.html', context)

