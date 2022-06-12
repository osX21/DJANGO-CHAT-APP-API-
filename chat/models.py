from django.db import models
from django.contrib.auth import get_user_model
from message.models import Message

class ChatRoom(models.Model):
    user1 = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='user1')
    user2 = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='user2')
    messages = models.ManyToManyField(Message, related_name='messages', blank=True, null=True)

    def __str__(self):
        return f'{self.user1} <=> {self.user2}'