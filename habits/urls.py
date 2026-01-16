from django.urls import path

from habits.views import HabitListView, HabitCreateView, HabitPublicListView

urlpatterns = [
    path('habits/', HabitListView.as_view(), name='habit_list'),
    path('habits/create/', HabitCreateView.as_view(), name='habit_create'),
    path('habits/public/', HabitPublicListView.as_view(), name='habit_public_list')
    ]