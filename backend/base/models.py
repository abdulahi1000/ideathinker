from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=True) 
    last_name = models.CharField(max_length=50, null=True) 
    phone_number = models.CharField(max_length=20, null=True) 
    email = models.CharField(max_length=30, null=True) 
    profile_pic = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}' 
