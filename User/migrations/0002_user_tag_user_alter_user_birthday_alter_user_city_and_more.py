# Generated by Django 4.2.13 on 2024-06-03 19:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='tag_user',
            field=models.CharField(max_length=20, null=True, verbose_name='Тег'),
        ),
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, max_length=85, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='user',
            name='country',
            field=models.CharField(blank=True, max_length=60, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='user',
            name='friends',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='Друзья'),
        ),
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='users/%Y/%m/%d/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='user',
            name='telephone_number',
            field=models.CharField(max_length=20, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='user',
            name='title',
            field=models.TextField(blank=True, max_length=50, verbose_name='О пользователе'),
        ),
    ]
