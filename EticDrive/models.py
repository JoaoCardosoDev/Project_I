from django.contrib.auth.models import AbstractUser
from django.db import models

class NormalUser(AbstractUser):
    email = models.EmailField(unique=True)
    max_quota = models.IntegerField(default=50)
    quota_counter = models.IntegerField(default=0)
    
    def get_quota_counter(self):
        return self.quota_counter