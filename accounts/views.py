from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import CustomLoginForm, CreatingUserFrom
from django.contrib import messages

def custom_login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # redirect to your dashboard/home
        else:
            messages.error(request, "Invalid username or password")
    else:
        form = CustomLoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def custom_logout_view(request):
    logout(request)
    return redirect('login')  # redirect to login page

def custom_register_view(request):
    if request.method == 'POST':
        form = CreatingUserFrom(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created. Please login.")
            return redirect('login')
    else:
        form = CreatingUserFrom()
    return render(request, 'accounts/register.html', {'form': form})
