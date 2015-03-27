from django import forms
from django.forms import ModelForm
from mythread.models import Thread
#from blog.models import Replay

class ThreadForm(ModelForm):
    class Meta:
        model = Thread
        widgets = {

        }
