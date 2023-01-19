from django.contrib import admin
from .views import *
from .templates import *
from django.urls import path,include

urlpatterns = [
    path('register/', RegisterUser),
    path('login/', LoginUser),
    path('logout/', logout_view),
    path('login_2/', mylogin ),
    path('addtodo/', addTodo ),
    
    # path('',include('home.urls')),
]
