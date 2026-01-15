from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """ модель Пользователей"""
    email = models.EmailField(max_length=35, unique=True, help_text="Введите email")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
