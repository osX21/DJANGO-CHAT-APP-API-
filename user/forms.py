from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *
from django import forms


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label = '',
        widget = forms.TextInput(attrs={
            'class': 'form-control', 'placeholder': 'Username'
        })
    )
    name = forms.CharField(
        label = '',
        widget=forms.TextInput(attrs={
            'class': 'form-control', 'placeholder': 'Name'
        })
    )
    password1 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password',
        })
    )
    password2  = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm Password'
        })
    )
    class Meta:
        model = CustomUser
        fields = ('username', 'name')

        # widgets = {
        #     'username': forms.TextInput(attrs={'class': 'form-control',
        #     'id': 'nombre', 'placeholder':  'Username'}),
        #     'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'nombre', 'placeholder': 'Your Name '})
        # }

        help_texts = {
            'username': None,
            'name': None
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text=None
        self.fields['password2'].help_text=None

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'name', )