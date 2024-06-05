from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Base(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=30)
    path = models.CharField(max_length=80)

class Root(Base):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

class Folder(Base):
    parent = models.ForeignKey(Root, on_delete=models.CASCADE)

class File(Base):
    parent = models.ForeignKey(Folder, on_delete=models.CASCADE)
    storage = models.FileField(upload_to='storage')