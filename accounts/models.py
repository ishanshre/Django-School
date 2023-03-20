from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=255)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    avatar = models.ImageField(upload_to="auth/profile/avatar", null=True, blank=True)
    bio = models.TextField(max_length=10000, null = True, blank=True)
    position  = models.CharField(max_length=100, null=True, blank=True)
    phone = PhoneNumberField(null=True, blank=True)
    address = models.CharField(null=True, blank=True, max_length=255)
    def __str__(self):
        return f"{self.user.username}'s profile"