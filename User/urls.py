from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


app_name = 'User'

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('profile/', views.UserProfile.as_view(), name='profile'),
    path('registration/', views.RegisterUser.as_view(), name='regist'),
    path('settings/', views.SettingsUser.as_view(), name='settings'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
