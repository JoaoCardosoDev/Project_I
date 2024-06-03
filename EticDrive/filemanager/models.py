from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Folder(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=30)
    path = models.CharField()

class File(models.Model):
    id = models.BigAutoField(primary_key=True)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    path = models.CharField()