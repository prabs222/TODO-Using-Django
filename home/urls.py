from django.contrib import admin
from .views import RegisterUser,LoginUser,logout_view
from django.urls import path,include

urlpatterns = [
    path('register/', RegisterUser),
    path('login/', LoginUser),
    path('logout/', logout_view),
    
    # path('',include('home.urls')),
]
