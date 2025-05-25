from django.db import models
from django.contrib.auth.models import User
from datetime import time


class CustomUser(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        # show multiple fields in the admin panel
        return f"{self.first_name} {self.last_name} ({self.username})"
    
