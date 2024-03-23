from .models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
#created is a boolean value
def post_save_create_profile(sender, instance, created, *args, **kwargs):
  print(sender)
  print(instance)
  print(created)
  # If the created is true, then create a profile 
  if created:
    #user was been defined in the models.py
    Profile.objects.create(user=instance)