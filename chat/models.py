from django.conf import settings
from django.db import models

from account.models import User

# Create your models here.


class ChatRoom(models.Model):
    name = models.CharField(max_length=255)
    users = models.ManyToManyField(User, related_name='chat_rooms')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='server_owner')
    topic = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        super(ChatRoom, self).save(*args, *kwargs)

    def __str__(self):
        return self.name
    
class ChatMessage(models.Model):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(null=False)
    timestamp = models.DateTimeField(auto_now_add=True)    