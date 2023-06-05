from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm

#https://docs.djangoproject.com/en/1.8/_modules/django/contrib/auth/forms/#UserCreationForm
class UserRegistrationForm(UserCreationForm):
    error_messages = {
        'password_mismatch': ("The two password fields didn't match.")
    }
    class Meta:
        model=User
        fields = ['username', 'email', 'password1', 'password2']
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'type': 'text',
        'class': 'username',
    }))
    password = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Password',
        'type': 'text',
        'class': 'password',
    }))
