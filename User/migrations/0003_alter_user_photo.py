# Generated by Django 4.2.13 on 2024-06-03 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_user_tag_user_alter_user_birthday_alter_user_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, default='users/default.jpg', null=True, upload_to='users/%Y/%m/%d/', verbose_name='Фото'),
        ),
    ]
