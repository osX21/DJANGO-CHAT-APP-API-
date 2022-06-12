from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    name = models.CharField(max_length=50)
    chatrooms = models.ManyToManyField('chat.ChatRoom', related_name='rooms')
