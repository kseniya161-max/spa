from django.core.exceptions import ValidationError
from django.db import models
from users.models import User


class Habit(models.Model):
    """Модель Полезная привычка"""

    name = models.CharField(max_length=150, unique=True, help_text="Название привычки")
    user = models.ForeignKey(
        User, related_name="habits", on_delete=models.CASCADE, help_text="Пользователь"
    )
    place = models.ForeignKey(
        "Place", on_delete=models.CASCADE, help_text="Место выполнения привычки"
    )
    time = models.TimeField(help_text="Время выполнения привычки")
    action = models.CharField(
        max_length=250, help_text="Действие связанное с привычкой"
    )
    pleasant_habit = models.ForeignKey(
        "PleasantHabit",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="pleasant_habits",
        help_text="Приятная привычка",
    )
    periodic = models.PositiveIntegerField(
        default=1, help_text="Периодичность выполнения привычки в днях"
    )
    reward = models.CharField(
        max_length=250, null=True, blank=True, help_text="Вознаграждение за привычку"
    )
    duration = models.PositiveIntegerField(help_text="Время на выполнение в секундах")
    is_public = models.BooleanField(default=False, help_text="Публичность")
    related_habit = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        related_name="related_habits",
        on_delete=models.SET_NULL,
        help_text="Связанная привычка",
    )

    def clean(self):
        """Метод Валидации"""
        if self.reward and self.pleasant_habit:
            raise ValidationError(
                "Нельзя одновременно указывать и Связанную привычку и Вознаграждение"
            )

        if self.duration > 120:
            raise ValidationError("Время не должно привышать 120 секунд")

        if self.pleasant_habit and (self.reward or self.related_habit):
            raise ValidationError(
                "Приятная привычка не должна иметь вознаграждения или связанной привычки"
            )

        if self.related_habit and not self.related_habit.is_pleasant:
            raise ValidationError(
                "В связанные привычки могут попадать только привычки с признаком приятной привычки."
            )

        if self.periodic < 7:
            raise ValidationError("Нельзя выполнять привычку реже, чем 1 раз в 7 дней.")

    def __str__(self):
        return f"{self.name} пользователя {self.user}"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"


class Place(models.Model):
    """Модель Место"""

    name = models.CharField(
        max_length=150, unique=True, help_text="Место выполнения привычки"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Место"
        verbose_name_plural = "Места"


class PleasantHabit(models.Model):
    """Модель Приятная Привычка"""

    name = models.CharField(
        max_length=150, unique=True, help_text="Имя приятной привычки"
    )
    is_pleasant = models.BooleanField(
        default=True, help_text="Признак приятной привычки"
    )
    user = models.ForeignKey(
        User,
        related_name="pleasant_habits",
        on_delete=models.CASCADE,
        help_text="Пользователь приятной привычки",
    )

    def __str__(self):
        return f"{self.name} пользователя {self.user}"

    class Meta:
        verbose_name = "Приятная привычка"
        verbose_name_plural = "Приятные привычки"
