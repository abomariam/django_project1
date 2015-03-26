from django import forms
from django.forms import ModelForm
#from blog.models import Thread
from replay.models import Replay

class ReplayForm(ModelForm):
    class Meta:
        model = Replay
        widgets = {

        }