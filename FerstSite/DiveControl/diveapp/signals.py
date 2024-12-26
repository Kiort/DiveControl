from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Diver

@receiver(post_save, sender=User)
def create_diver_profile(sender, instance, created, **kwargs):
    if created:
        Diver.objects.create(user=instance)