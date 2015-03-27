from django.db import models
from user.models import User
from django import forms


# Create your models here.
class Messages(models.Model):
    body = models.TextField()
    sender = models.ForeignKey(User, related_name='messages_sender')
    reciever = models.ForeignKey(User, related_name='messages_reciever')
    time = models.DateTimeField(auto_now_add=True)

class MessageForm(forms.ModelForm):
    class Meta:
        model=Messages
