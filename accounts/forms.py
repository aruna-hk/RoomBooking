from django.contrib import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'


