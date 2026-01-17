
from rest_framework import serializers

from habits.models import Habit, Place, PleasantHabit


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'


        def validate(self, data):
            habit = Habit(**data)
            habit.clean()
            return data


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'


class PleasantHabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = PleasantHabit
        fields = '__all__'


