from django.shortcuts import render
from django.views.generic import TemplateView,FormView,DetailView
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse_lazy,reverse
from django.db.models import Count,Avg
from datetime import datetime

# App models and forms
from .models import Team,UserProfile,HappinessLevel
from .forms import HappinessLevelForm

# Exceptions
from django.core.exceptions import ObjectDoesNotExist

class UserAlreadyAnswered(Exception):
    def __init__(self):
        pass

# Index View
class IndexView(TemplateView):
    template_name = 'happiness_app/index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)

        try:
            # Gets the UserProfile by the user logged in.
            # If the user is not registered in UserProfile, the ObjectDoesNotExist will raise
            user_profile_id = UserProfile.objects.get(user=self.request.user.id)
            context['user_in_profile'] = True

            # Gets the UserProfile, Team, Users from the teams, and today's date
            team_id = user_profile_id.team_id
            team_users = UserProfile.objects.filter(team_id=team_id)
            today = datetime.today().date()

            # Verifies if the user already answer the pool today
            context['user_answer_today'] = HappinessLevel.objects.filter(user_id=user_profile_id,date=today)

            # Sets the filters to date and team (if it exists)
            filter_kwargs = {
                'date':today,
            }

            if team_id != None:
                filter_kwargs['user_id__in'] = team_users

            # Count of all levels of happiness and their average
            context['answer_level_1'] = HappinessLevel.objects.filter(level=1,**filter_kwargs).count()
            context['answer_level_2'] = HappinessLevel.objects.filter(level=2,**filter_kwargs).count()
            context['answer_level_3'] = HappinessLevel.objects.filter(level=3,**filter_kwargs).count()
            context['answer_level_4'] = HappinessLevel.objects.filter(level=4,**filter_kwargs).count()
            context['answer_level_5'] = HappinessLevel.objects.filter(level=5,**filter_kwargs).count()
            context['average'] = HappinessLevel.objects.values('date').filter(**filter_kwargs).annotate(level_avg=Avg('level'))

        # If the user is not in UserProfile, this user cannot register the happiness level
        except ObjectDoesNotExist:
            context['user_answer_today'] = None
            context['user_in_profile'] = False
        # Other errors
        except:
            return HttpResponse("An unknown error has occurred.")

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
                # Gets the UserProfile by the user logged in.
                # If the user is not registered in UserProfile, the ObjectDoesNotExist will raise
                user_profile_id = UserProfile.objects.get(user=self.request.user.id)
                today = datetime.today().date()

                if HappinessLevel.objects.filter(user_id=user_profile_id,date=today):
                    raise UserAlreadyAnswered

                happy = form.save(commit=False)
                happy.user_id = user_profile_id
                happy.save()

                return HttpResponseRedirect(self.success_url)

            except UserAlreadyAnswered:
                return HttpResponseRedirect(reverse('ans_error'))
            # If the user is not in UserProfile, this user cannot register the happiness level
            except ObjectDoesNotExist:
                return HttpResponseRedirect(reverse('reg_error'))
            # Other errors
            except:
                return HttpResponseRedirect(reverse('error'))

        return render(request, self.template_name, {'form': form})

class ErrorView(TemplateView):
    template_name = 'happiness_app/error.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['error'] = "This user is not registered to submit the happiness level."

        return context

class AnswerErrorView(TemplateView):
    template_name = 'happiness_app/error.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['error'] = "This user already answered the pool today."

        return context
