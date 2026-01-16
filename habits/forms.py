from django import forms

from habits.models import Habit


class HabitCreateForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ('name', 'action', 'duration', 'is_public', 'place', 'pleasant_habit', 'periodic', 'reward')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Название привычки'}),
            'action': forms.TextInput(attrs={'placeholder': 'Действие'}),
            'duration': forms.NumberInput(attrs={'placeholder': 'Время на выполнение (в секундах)'}),
            'is_public': forms.CheckboxInput(),
            'place': forms.Select(),
            'pleasant_habit': forms.Select(),
            'periodic': forms.NumberInput(attrs={'placeholder': 'Периодичность (в днях)'}),
            'reward': forms.TextInput(attrs={'placeholder': 'Вознаграждение'}),
        }