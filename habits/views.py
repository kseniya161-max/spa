from django.shortcuts import render
from django.views.generic import ListView

from habits.models import Habit


class HabitListView(ListView):
    model = Habit
    template_name = 'habits/habits_list.html'
    context_object_name = 'habits'
    paginate_by = 5


    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)
    
