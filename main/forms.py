from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm


class AiForm(forms.Form):
    text = forms.CharField(max_length=255)\

    widgets = {'text': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Введите ваш запрос'})
    }



class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    widgets = {'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder':  'Введите логин'}),
               'email':forms.TextInput(attrs={'class': 'form.control', 'placeholder': 'Введите email адрес'}),
               'password': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль'})

    }