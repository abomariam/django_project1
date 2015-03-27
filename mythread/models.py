from django.db import models
from django_countries.fields import CountryField
from user.models import *
from cat_forum.models import *
# Create your models here.

class Thread(models.Model):
    title = models.CharField(max_length=200, default=" ")
    author = models.ForeignKey(User)
    forum = models.ForeignKey(Forum)
    sticky = models.BooleanField(default=False)
    lock = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
