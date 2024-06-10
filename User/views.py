from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from User.forms import UserAuthoriateForm, RegistrationUserForm, SettingFormUser
from django.views.generic import CreateView, DetailView, UpdateView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model


class HomePage(TemplateView):
    template_name = 'User/home.html'


class UserProfile(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = 'User/profile.html'
    context_object_name = 'post'
    
    def get_object(self, queryset=None):
        return self.request.user


class RegisterUser(CreateView):
    form_class = RegistrationUserForm
    template_name = 'User/register.html'
    success_url = reverse_lazy('User:login')


class LoginUser(LoginView):
    form_class = UserAuthoriateForm
    template_name = 'User/login.html'


class SettingsUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    template_name = "User/settings.html"
    form_class = SettingFormUser
    extra_context = {
        'title': 'Настройки'
    }
    
    def get_object(self, queryset: QuerySet[Any] | None = ...) -> Model:
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('user:profile')


def got_404(request, exception):
    return HttpResponse('<h1>Ошибка 404, Пользователь с таким тегом не найден</h1>')