from django.contrib import admin

from habits.models import Habit, Place, PleasantHabit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ("name", "is_public", "user", "place")
    search_fields = ("name", "user__username", "place__name")
    list_filter = ("is_public", "user")
    ordering = ("name",)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(PleasantHabit)
class PleasantHabitAdmin(admin.ModelAdmin):
    list_display = ("name", "is_pleasant", "user")
    search_fields = ("name", "user__username")
    list_filter = ("is_pleasant", "user")
