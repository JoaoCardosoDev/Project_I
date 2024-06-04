from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from EticDrive.views import Login, Signup
from filemanager.views import root

urlpatterns = [
    path("", root, name="root")
]
