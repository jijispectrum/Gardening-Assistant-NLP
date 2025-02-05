from django.urls import path
from .views import home,index,user_login,user_register,user_logout

urlpatterns = [
    path('', index, name='index'),
    path('login/', user_login, name='login'),
    path('register', user_register, name='register'),
    path('logout/', user_logout, name='logout'),
    path('home/', home, name='home'),
    
]
