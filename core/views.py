from django.shortcuts import render, redirect
from courses.models import Course
from .forms import RegisterForm
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile

def home(request):
    courses = Course.objects.all()[:6]
    return render(request, 'core/home.html', {'courses': courses})
def about(request):
    return render(request, 'core/about.html')
def contact(request):
    return render(request, 'core/contact.html')
def profile(request):
    return render(request, 'core/profile.html')

def login_register(request):
    if request.method == 'POST':
        if 'login' in request.POST:
            # Handle login
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('login')

        elif 'register' in request.POST:
            # Handle registration
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            number = request.POST.get('number')

            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('login')
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
                return redirect('login')

            user = User.objects.create_user(username=username, email=email, password=password)
            # Optional: store extra info in Profile
            Profile.objects.create(user=user, bio=f"Phone: {number}")
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')

    return render(request, 'registration/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')