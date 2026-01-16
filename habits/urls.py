from django.urls import path

from habits.views import HabitListView, HabitCreateView, HabitPublicListView, HabitUpdateView, HabitDeleteView

urlpatterns = [
    path('habits/', HabitListView.as_view(), name='habit_list'),
    path('habits/create/', HabitCreateView.as_view(), name='habit_create'),
    path('habits/public/', HabitPublicListView.as_view(), name='habit_public_list'),
    path('habits/update/<int:pk>/', HabitUpdateView.as_view(), name='habit_update'),
    path('habits/delete/<int:pk>/', HabitDeleteView.as_view(), name='habit_delete'),
    ]