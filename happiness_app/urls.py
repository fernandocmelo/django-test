from django.urls import path
from . import views

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('login/',views.UserLogin.as_view(),name='user_login'),
    path('logout/',views.UserLogout,name='user_logout'),
]
