from django.shortcuts import render
from django.views.generic import TemplateView,FormView,RedirectView
from .models import Team,UserProfile,HappinessLevel

#User control
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
class IndexView(TemplateView):
    template_name = 'happiness_app/index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)

        return context

class UserLogin(TemplateView):
    template_name = 'happiness_app/login.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)

        return context

class UserLogout(RedirectView):

    url = 'happiness_app/index.html'

    def get(self,request):
        logout(request)
        return HttpResponseRedirect(reverse('index'))
