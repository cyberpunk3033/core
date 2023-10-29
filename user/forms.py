from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Task, CustomUser


class TaskForm(forms.ModelForm):
    executor = forms.ModelChoiceField(queryset=CustomUser.objects.all())

    class Meta:
        model = Task
        fields = ('title', 'description', 'executor', 'completion_date')



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2')