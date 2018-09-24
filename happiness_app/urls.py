from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

login_view = 'happiness_app/login.html'

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('login/',auth_views.LoginView.as_view(template_name=login_view),name='user_login'),
    path('logout/',auth_views.LogoutView.as_view(),name='user_logout'),
    path('happiness/',views.RegisterHappiness.as_view(),name='register_happiness'),
]
