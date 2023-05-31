from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

#https://docs.djangoproject.com/en/1.8/_modules/django/contrib/auth/forms/#UserCreationForm
class UserRegistration(UserCreationForm):
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
