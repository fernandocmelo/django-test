from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

# Sets the default HTML for login
login_view = 'happiness_app/login.html'

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('login/',auth_views.LoginView.as_view(template_name=login_view),name='user_login'),
    path('logout/',auth_views.LogoutView.as_view(),name='user_logout'),
    path('register/',views.RegisterHappiness.as_view(),name='register_happiness'),
    path('error_reg/',views.ErrorView.as_view(),{'error':'reg_error'},name='reg_error'),
    path('error_answer/',views.ErrorView.as_view(),{'error':'ans_error'},name='ans_error'),
    path('error/',views.ErrorView.as_view(),{'error':'error'},name='error'),
]
