# from django.urls import path
#
# from habits.views import HabitListView, HabitCreateView, HabitPublicListView, HabitUpdateView, HabitDeleteView
#
# urlpatterns = [
#     path('habits/', HabitListView.as_view(), name='habit_list'),
#     path('habits/create/', HabitCreateView.as_view(), name='habit_create'),
#     path('habits/public/', HabitPublicListView.as_view(), name='habit_public_list'),
#     path('habits/update/<int:pk>/', HabitUpdateView.as_view(), name='habit_update'),
#     path('habits/delete/<int:pk>/', HabitDeleteView.as_view(), name='habit_delete'),
#     ]
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from habits.views import HabitViewSet, PleasantHabitViewSet

router = DefaultRouter()
router.register(r'habits', HabitViewSet, basename='habit')
router.register(r'pleasent_habit', PleasantHabitViewSet, basename='pleasent_habits')


urlpatterns = [
    path('', include(router.urls)),
]
