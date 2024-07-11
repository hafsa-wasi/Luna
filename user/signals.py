#for signals  1.write the below code.  2.Write something in init.py(app) 3.apps.py

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import profile

@receiver(post_save, sender = User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile.objects.create(user = instance)






# @receiver(post_save, sender = signup)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         profile.objects.create(user = instance)
#         #profile.objects.create(Email = instance)