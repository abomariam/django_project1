from django.db import models
from django import forms


class Category(models.Model):
    name = models.CharField(max_length=25, unique=True)
    lock = models.BooleanField(max_length=10, default=False)

    def __str__(self):
        return self.name


class Forum(models.Model):
    name = models.CharField(max_length=25, unique=True)
    lock = models.BooleanField(max_length=10, default=False)
    category = models.CharField(max_length=10)
    category = models.ForeignKey(Category)


class CatForm(forms.ModelForm):
    class Meta:
        model = Category


class ForumForm(forms.ModelForm):
    class Meta:
        model = Forum

