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
            return redirect('home') #TASK: Change this to hastalar view

    return render(request,'hasta/add_hasta.html',{'hastaForm':hastaForm,'kateterOlayiForm':kateterOlayiForm})
