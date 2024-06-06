from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from filemanager.views import create_folder, home

urlpatterns = [
    path("", create_folder, name="index"),
    path("home/", home, name="home")
]
