from django.db import models
from user.models import User
from django import forms


# Create your models here.
class messages(models.Model):
    body = models.CharField(max_length=25)
    sender = models.ForeignKey(User, related_name='messages_sender')
    reciever = models.ForeignKey(User, related_name='messages_reciever')


class MessageForm(forms.ModelForm):
    class Meta:
        model=messages
