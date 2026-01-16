from django.urls import path

from habits.views import HabitListView

urlpatterns = [
    path('habits/', HabitListView.as_view(), name='habit_list'),
    ]