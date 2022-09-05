from audioop import reverse
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import UserRegistrationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import CreateView

class CreateUserView(CreateView):
    model = User
    template_name='registration/create_user.html'
    fields = ('username', 'password')
    success_url = reverse_lazy('dashboard')


def dashboard(request):
    return render(request, 'users/dashboard.html')

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    # success_url = reverse_lazy('dashboard')
    success_url = reverse_lazy('password_success')
def password_success(request):
    return render(request, 'registration/password_success.html')
# def home(request):
#     return render(request, 'users/home.html')


# def register(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()

#             messages.success(request, f'Your account has been created. You can log in now.')
#             return redirect('login')
#     else:
#         form =UserRegistrationForm()
    
#     return render(request, 'users/register.html', {'form': form})

