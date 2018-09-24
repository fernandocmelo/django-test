from django.shortcuts import render
from django.views.generic import TemplateView,FormView
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse_lazy
from datetime import datetime

# App models and forms
from .models import Team,UserProfile,HappinessLevel
from .forms import HappinessLevelForm

# Exceptions
from django.core.exceptions import ObjectDoesNotExist

# Index View
class IndexView(TemplateView):
    template_name = 'happiness_app/index.html'

    def get_context_data(self,**kwargs):
       context = super().get_context_data(**kwargs)

       try:
           # user_profile_id = UserProfile.objects.get(user=request.user.id)
           # user_id=user_profile_id,
           context['user_answer_today'] = HappinessLevel.objects.filter(date=datetime.today().date()).first()
           print("try")
       except ObjectDoesNotExist:
           context['user_answer_today'] = None
           print("except")

       return context
# View to register the happiness level
class RegisterHappiness(FormView):
     template_name = 'happiness_app/happy.html'
     form_class = HappinessLevelForm
     model = HappinessLevel
     success_url = reverse_lazy('index')

     def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

     def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            try:
                happy = form.save(commit=False)
                # Get the UserProfile object by User.id
                happy.user_id = UserProfile.objects.get(user=request.user.id)
                happy.save()
                return HttpResponseRedirect(self.success_url)
            except ObjectDoesNotExist:
                return HttpResponse("This user is not registered to submit the happiness level.")
            except:
                return HttpResponse("An unknown error has occurred.")

        return render(request, self.template_name, {'form': form})
