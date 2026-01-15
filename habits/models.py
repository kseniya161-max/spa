from django.db import models

from users.models import User


class Habit(models.Model):
    """ Модель привычка"""
    name = models.CharField(max_length=150, unique=True, help_text='Название привычки')
    user = models.ForeignKey(User, related_name='habit', help_text='Пользователь')
    place = models.CharField(max_length=200,  help_text='Место выполнения привычки')
    time = models.TimeField(help_text='Время выполнения привычки')
    action = models.CharField(max_length=250, help_text='Действие связанное с привычкой')
    pleasant_habit = models.ForeignKey(PleasantHabit,related_name='PleasantHabit', help_text='Полезная привычка')
    periodic = models.PositiveIntegerField(default=1, help_text='Периодичность выполнения привычки в днях')
    reward = models.CharField(max_length=250, null=True, blank=True, help_text='Вознаграждение за привычку')
    time_to_complete = models.PositiveIntegerField(help_text='Время на выполнение в секундах')
    is_public = models.BooleanField(default=False, help_text='Публичность')


class Place(models.Model):
    """Модель Место"""
    name = models.CharField(max_length=150, unique=True, help_text='Место выполнения привычки')


class PleasantHabit(models.Model):
    """ Модель Полезная Привычка"""