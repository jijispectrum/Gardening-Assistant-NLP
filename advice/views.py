from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Query
from .utils import get_gardening_advice
from django.contrib.auth.decorators import login_required

def index(request):
    """ Renders the index page """
    return render(request, 'advice/index.html')

@login_required
def home(request):
    """ Handles gardening advice and stores user chat history """
    response = None
    chat_history = Query.objects.filter(user=request.user).order_by('-timestamp')[:10]  # Fetch last 10 queries

    if request.method == 'POST':
        question = request.POST.get('question')
        response = get_gardening_advice(question)
        Query.objects.create(user=request.user, question=question, response=response)

    return render(request, 'advice/home.html', {'response': response, 'chat_history': chat_history})
@login_required
def clear_chat_history(request):
    """ Deletes all chat history for the logged-in user """
    Query.objects.filter(user=request.user).delete()
    messages.success(request, 'Chat history cleared!')

    return redirect('home')
def user_login(request):
    """ Handles user login """
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password.')
    return redirect('index')

def user_register(request):
    """ Handles user registration """
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
    """ Logs out the user """
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('index')
from django.shortcuts import render
from .models import ChatHistory

def chat_history(request):
    chat_history = Query.objects.filter(user=request.user).order_by('-timestamp')
    return render(request, 'advice/history.html', {'chat_history': chat_history})
