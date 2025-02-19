from django.urls import path
from .views import home,index,user_login,user_register,user_logout,clear_chat_history
from .views import chat_history
urlpatterns = [
    path('', index, name='index'),
    path('login/', user_login, name='login'),
    path('register', user_register, name='register'),
    path('logout/', user_logout, name='logout'),
    path('home/', home, name='home'),
    path('clear-chat/',clear_chat_history, name='clear_chat_history'),
    path('history/', chat_history, name='chat_history'),
        # Clear chat history
    
]
