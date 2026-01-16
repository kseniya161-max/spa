from django.shortcuts import render, redirect
from django.views import View

from users.forms import CustomUsersCreationForm


class RegistrationView(View):
    def get (self, request):
        form = CustomUsersCreationForm()
        return render(request, 'users/registration.html', {'form': form})


    def post(self, request):
        form = CustomUsersCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render (request, 'users/registration.html', {'form': form} )


