from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from .utils import user_directory_path

# Create your models here.
class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=user_directory_path, null= True, default='/wuthering.jpg' )
    email = models.EmailField()

    def __str__(self):
        return f'{self.user.username}\'s Profile'
    




