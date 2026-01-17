# from django.contrib.auth import authenticate, login
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.shortcuts import render, redirect
# from django.urls import reverse_lazy
# from django.views import View, generic
#
# from users.forms import CustomUsersCreationForm
# from users.models import User
#
#
# class RegistrationView(generic.CreateView):
#     model = User
#     form_class = CustomUsersCreationForm
#     template_name = 'users/registration.html'
#     success_url = reverse_lazy('login')
#     def form_valid(self, form):
#
#         return super().form_valid(form)
#
#
# class LoginView(View):
#     def get(self, request):
#         form = AuthenticationForm()
#         return render(request, 'users/login.html', {'form': form})
#
#     def post(self, request):
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')  # Замените 'home' на нужный URL после входа
#         return render(request, 'users/login.html', {'form': form})
#
#
