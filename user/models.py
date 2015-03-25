from django.db import models
from django_countries.fields import CountryField
# Create your models here.



class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    gender = models.CharField(max_length=1, choices=(
        ('m','Male'),
        ('f','Female')
        ), default='m')

    is_banned = models.BooleanField(default=False, verbose_name="Banned")

    role = models.CharField(max_length=1, choices=(
        ('r','Regular'),
        ('a','Admin')
        ),default='r')

    country = CountryField(default='EG')

    signature = models.TextField(blank=True)
