from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from filemanager.views import create_folder, download, home, deleteInstance, editInstance, root

urlpatterns = [
    path("", root, name="root"),
    path("home/", home, name="home"),
    path("delete/<str:id>", deleteInstance, name='deleteInstance'),
    path("edit/<str:id>", editInstance, name='editInstance'),
    path("download/<str:id>", download, name='download')
]
