from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class User(AbstractUser):
    title = models.TextField(max_length=50, blank=True, verbose_name='О пользователе')
    birthday = models.DateField(verbose_name='Дата рождения')
    photo = models.ImageField(upload_to="users/%Y/%m/%d/", blank=True, null=True, verbose_name='Фото')
    country = models.CharField(max_length=60, blank=True, verbose_name='Страна')
    city = models.CharField(max_length=85, blank=True, verbose_name='Город')
    tag_user = models.CharField(max_length=20, verbose_name='Тег', null=True)
    telephone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
    