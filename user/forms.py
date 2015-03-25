from django import forms
from django.forms import ModelForm,Form
from user.models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        widgets = {
            'password': forms.PasswordInput(),
            # 'gender' : forms.RadioSelect(),
            'signature': forms.Textarea(attrs={'rows':3}),
        }

class LoginForm(Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())