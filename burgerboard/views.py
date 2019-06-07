from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.core.exceptions import *
from datetime import datetime, timedelta, timezone

from .models import Login
from .models import Interest
from .models import Maxinterest
from .models import Mealdate

# Create your views here.

def index(request):
    return HttpResponseRedirect('homepage')



class homepage(generic.TemplateView):
    template_name = 'burgerboard/index.html'

class signupview(generic.TemplateView):
    template_name = 'burgerboard/sign_up.html'

def signupcomplete(request):
    try:
        selected_username = request.POST['Username']
        selected_password = request.POST['Password']
    except (KeyError):
        return HttpResponseRedirect("")

    else:
        login = Login()
        login.username_text = selected_username
        login.password_text = selected_password
        login.save()
        return HttpResponseRedirect("/burgerboard")

class loginview(generic.TemplateView):
    template_name = 'burgerboard/log_in.html'

def logincomplete(request):
    
    try:
        entered_username = request.POST['Username']
        entered_password = request.POST['Password']
        check = Login.objects.get(username_text=entered_username,password_text=entered_password)
    except (KeyError, ObjectDoesNotExist):
        return HttpResponseRedirect("/burgerboard/login")

    else:
        login = Login()
        login.username_text = entered_username
        login.password_text = entered_password
        
        return HttpResponseRedirect("/burgerboard/loggedin")

class loggedin(generic.TemplateView):
    template_name = 'burgerboard/loggedin.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Interest'] = Interest.objects.all()
        context['InterestMax'] = Maxinterest.objects.first()
        context['InterestCut']  = Maxinterest.objects.first()
        context['Mealtime'] = Mealdate.objects.first()
        return context
    


def formcomplete(request):
    try:
        if datetime.now(timezone.utc) < Maxinterest.objects.first().cutoff_date: 
            selected_firstname = request.POST['firstname']
        else: 
            raise KeyError
    except (KeyError):
        return HttpResponseRedirect("/burgerboard/loggedin")

    else:
        interest = Interest()
        interest.name = selected_firstname
        interest.save()
        return HttpResponseRedirect("/burgerboard/loggedin")

