from django.contrib.auth.models import User
from django import forms
from .models import Memea


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class MemeaForm(forms.ModelForm):

    class Meta:
        model = Memea
        fields = ['izenburua', 'argazkia']

