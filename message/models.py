from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime

class Message(models.Model):
    text = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)
    chatroom = models.ForeignKey('chat.ChatRoom', on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    def get_date(self):
        time = datetime.now()
        if time.day == self.date.day:
            return str(time.hour - self.date.hour) + ' hours ago'
        else:
            if self.month == time.month:
                return str(time.day - self.date.day) + ' days ago'
        return self.date
    
    def __str__(self):
        return self.text