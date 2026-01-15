from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """ модель Пользователей"""
    email = models.EmailField(max_length=35, unique=True, help_text="Введите email")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text='Группы, к которым принадлежит пользователь.',
        verbose_name='Группы'
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',
        blank=True,
        help_text='Разрешения, которые у пользователя.',
        verbose_name='Разрешения'
    )

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
