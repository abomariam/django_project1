from django.db import models
from django import forms


class Category(models.Model):
    name = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.name


class Forum(models.Model):
    name = models.CharField(max_length=25)
    lock = models.BooleanField(max_length=10, default=False)
    category = models.ForeignKey(Category)
    class Meta:
        unique_together = ('name', 'category',)

    def __str__(self):
        return self.name


class CatForm(forms.ModelForm):
    class Meta:
        model = Category


class ForumForm(forms.ModelForm):
    class Meta:
        model = Forum
        unique_together = ('name', 'category')

