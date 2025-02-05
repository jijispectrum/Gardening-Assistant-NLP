from django.shortcuts import render
from .models import Query
from .utils import get_gardening_advice

def home(request):
    response = None
    if request.method == 'POST':
        question = request.POST.get('question')
        response = get_gardening_advice(question)
        Query.objects.create(question=question, response=response)

    return render(request, 'advice/home.html', {'response': response})


from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def index(request):
    return render(request, 'advice/index.html')

def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('home')  # Redirect to a dashboard page
        else:
            messages.error(request, 'Invalid email or password.')
    return redirect('index')

def user_register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=email).exists():
            messages.error(request, 'Email already exists!')
        else:
            user = User.objects.create_user(username=email, email=email, password=password, first_name=name)
            user.save()
            messages.success(request, 'Registration successful! You can now log in.')
    return redirect('index')

def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('index')
