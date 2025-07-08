from django.db.models.signals import post_save
from django.dispatch import receiver
from utils.email import send_verification_email

from _user.models import User


@receiver(post_save, sender=User)
def send_email(sender, instance, created, **kwargs):
    if created and not instance.is_active:
        print("signal received...")
        send_verification_email(instance)
