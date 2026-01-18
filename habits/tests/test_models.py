import pytest
from django.contrib.auth import get_user_model
from habits.models import Habit, PleasantHabit

User = get_user_model()

@pytest.mark.django_db
def test_habit_creation():
    user = User.objects.create_user(email='test@example.com', password='testpass')
    pleasant_habit = PleasantHabit.objects.create(name='Relax', user=user)
    habit = Habit.objects.create(
        name='Йога',
        user=user,
        place=None,
        time='07:00',
        action='Заняться йогой',
        pleasant_habit=pleasant_habit,
        periodic=1,
        reward='Выпить Капучино',
        duration=60,
        is_public=True
    )
    assert habit.name == 'Йога'
    assert habit.user.email == 'test@example.com'

@pytest.mark.django_db
def test_habit_string_representation():
    user = User.objects.create_user(email='test@example.com', password='testpass')
    habit = Habit.objects.create(name='Йога', user=user)
    assert str(habit) == 'Йога пользователя test@example.com'
