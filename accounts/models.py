from django.db import models

# Create your models here.
# models.py
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)  # Bio del usuario
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)  # Foto de perfil

    def __str__(self):
        return f'{self.user.username} Profile'
