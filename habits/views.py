# from django.shortcuts import render
# from django.views.generic import ListView, CreateView, UpdateView, DeleteView
#
# from habits.forms import HabitCreateForm
# from habits.models import Habit
#
#
# class HabitListView(ListView):
#     model = Habit
#     template_name = 'habits/habits_list.html'
#     context_object_name = 'habits'
#     paginate_by = 5
#
#
#     def get_queryset(self):
#         return Habit.objects.filter(user=self.request.user)
#
#
#
# class HabitPublicListView(ListView):
#     model = Habit
#     template_name = 'habits/habits_public_list.html'
#     context_object_name = 'habits_public'
#     paginate_by = 5
#
#
#     def get_queryset(self):
#         return Habit.objects.filter(is_public=True)
#
#
# class HabitCreateView(CreateView):
#     model = Habit
#     form_class = HabitCreateForm
#     template_name = 'habits/habits_create.html'
#     context_object_name = 'habits_create'
#     success_url = '/habits/'
#
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)
#
#
# class HabitUpdateView(UpdateView):
#     model = Habit
#     form_class = HabitCreateForm
#     template_name = 'habits/habits_update.html'
#     context_object_name = 'habits_update'
#     success_url = '/habits/'
#
#     def get_queryset(self):
#         return Habit.objects.filter(user=self.request.user)
#
#
# class HabitDeleteView(DeleteView):
#     model = Habit
#     template_name = 'habits/habits_delete.html'
#     context_object_name = 'habits_delete'
#     success_url = '/habits/'
#
#     def get_queryset(self):
#         return Habit.objects.filter(user=self.request.user)
#
#
#
