from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import Teacher, Pupil
from django import forms


class UserCreatrForm(UserCreationForm):
    class Meta:
        fields = '__all__'
        model = Teacher()