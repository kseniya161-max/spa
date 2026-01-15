from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """ модель Пользователей"""
    name = models.CharField(max_length=150, null=True, blank=True, help_text='Имя Пользователя')


    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        plural_verbose_name = 'Пользователи'
