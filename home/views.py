from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
def home(request):
    auth_form = AuthenticationForm()
    return render(request,"home/home.html",{"auth_form":auth_form,})
from django.views.generic.base import TemplateView

class ContactView(TemplateView):
    template_name = 'home/contact.html'