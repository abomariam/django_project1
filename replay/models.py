from django.db import models
#from django_countries.fields import CountryField
# from thread.models import Thread
from user.models import *
from thread.models import *

class Replay(models.Model):
    author = models.ForeignKey(User)
    body = models.TextField()
    thread = models.ForeignKey(Thread)
    time = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title