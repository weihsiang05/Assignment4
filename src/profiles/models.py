from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
  # each user can only have one profile
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  bio = models.TextField(blank=True)
  avatar = models.ImageField(default='avatar.png', upload_to='avatars')
  update = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"profile of the user {self.user.username}"