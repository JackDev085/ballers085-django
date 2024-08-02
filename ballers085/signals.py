from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import UserProfile
from django.core.exceptions import ValidationError

@receiver(pre_save, sender=User)
def check_unique_email(sender, instance, **kwargs):
    if User.objects.filter(email=instance.email).exclude(username=instance.username).exists():
        raise ValidationError(f'O email {instance.email} já está em uso.')

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
