import datetime

from typing import Any
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms.forms import ValidationError
from django.contrib.auth import authenticate


class UserAuthoriateForm(AuthenticationForm):
    def __init__(self, *args, **kwargs): # Применяем к полям формы свои стили
        super(UserAuthoriateForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'input'})
        self.fields['password'].widget.attrs.update({'class': 'input'})
    
    username = forms.CharField(label='Логин',
                               widget=forms.TextInput()
                               )
    
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput())
        
    class Meta:
        model = get_user_model()


    def clean_username(self) -> dict[str, Any]:
        username = self.cleaned_data['username']
        self.username = username
        
        if get_user_model().objects.filter(username=username).exists():
            return username
        
        raise ValidationError('Пользователя с таким username не существует')

    def clean_password(self) -> dict[str, Any]:
        password = self.cleaned_data['password']
        
        if authenticate(username=self.username, password=password):
            return password
        
        raise ValidationError('Проверьте имя пользователя или пароль. Оба поля могут быть чувствительны к регистру')
    
    
class RegistrationUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs): # Применяем к полям формы свои стили
        super(RegistrationUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'input'})
        self.fields['password1'].widget.attrs.update({'class': 'input'})
        self.fields['password2'].widget.attrs.update({'class': 'input'})
        self.fields['first_name'].widget.attrs.update({'class': 'input'})
        self.fields['last_name'].widget.attrs.update({'class': 'input'})
        self.fields['email'].widget.attrs.update({'class': 'input'})
        self.fields['telephone_number'].widget.attrs.update({'class': 'input art-stranger'})
        self.fields['birthday'].widget.attrs.update({'class': 'input'})
        self.fields['tag_user'].widget.attrs.update({'class': 'input'})
        
 
    username = forms.CharField(label='Логин')
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput())
    email = forms.EmailField(label='E-mail', max_length=256)
    this_year = datetime.date.today().year
    birthday = forms.DateField(widget=forms.SelectDateWidget(years=tuple(range(this_year - 100, this_year - 5))), label='День рождение')
    telephone_number = forms.CharField(max_length=20, label='Номер телефона')
    tag_user = forms.CharField(max_length=20, label='Тег')
    first_name = forms.CharField(label='Имя', max_length=30)
    last_name = forms.CharField(label='Фамилия', max_length=20)
    
    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'tag_user', 'telephone_number', 'birthday')
        
    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError('Такой E-mail уже существует')
        return email
    
    def clean_tag_user(self):
        user_tag = self.cleaned_data['tag_user']
        if get_user_model().objects.filter(tag_user=user_tag).exists():
            raise forms.ValidationError('Пользователь с таким тегом уже существует')
        return user_tag


class SettingFormUser(forms.ModelForm):
    username = forms.CharField(disabled=True, label='Логин')
    email = forms.EmailField(disabled=True, label='E-mail')
    first_name = forms.CharField(label='Имя', required=False, max_length=30)
    last_name = forms.CharField(label='Фамилия', required=False, max_length=20)
    tag_user = forms.CharField(max_length=20, label='Тег', required=False)
    title = forms.CharField(max_length=50, label='Описание профиля', required=False)
    country = forms.CharField(max_length=60, label='Страна', required=False)
    city = forms.CharField(max_length=85, label='Город', required=False)
    
    
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name',
                  'last_name', 'photo', 'tag_user',
                  'title', 'country', 'city',
                  'telephone_number')
        
        
    def clean_tag_user(self):
        user_tag = self.cleaned_data['tag_user']
        user_1 = get_user_model().objects.filter(tag_user=user_tag)
        if user_1.exists() and self.cleaned_data['username'] != user_1[0].username:
            raise forms.ValidationError('Пользователь с таким тегом уже существует')
        return user_tag