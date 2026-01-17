from django.db.migrations import serializer
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from habits.models import Habit, PleasantHabit
from habits.serializers import HabitSerializer, PleasantHabitSerializer


class CustomPagination(PageNumberPagination):
    page_size = 5


class HabitViewSet(ModelViewSet):
    serializer_class = HabitSerializer
    pagination_class = CustomPagination


    def get_queryset(self):
        user = self.request.user
        if self.request.user.is_authenticated:
            return Habit.objects.filter(user=user)
        return Habit.objects.filter(is_public=True)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PleasantHabitViewSet(ModelViewSet):
    serializer_class = PleasantHabitSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if self.request.user.is_authenticated:
            return PleasantHabit.objects.filter(user=user)
        return PleasantHabit.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



