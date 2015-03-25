from django import forms
from django.forms import ModelForm
from user.models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        widgets = {
            'password': forms.PasswordInput(),
            # 'gender' : forms.RadioSelect(),
            'signature': forms.Textarea(attrs={'rows':3}),
        }