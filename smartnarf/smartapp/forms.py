from .models import User
from django.forms import ModelForm, TextInput, CharField, PasswordInput


class UserLoginForm(ModelForm):
    login = CharField(label='login', widget=TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Повторите пароль'
            }))
    password = CharField(label='password', widget=PasswordInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Повторите пароль'
            }))


class UserRegisterForm(ModelForm):
    password2 = CharField(label='password2', widget=PasswordInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Повторите пароль'
            }))

    class Meta:
        model = User
        fields = ['name', 'login', 'password']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Введите имя',
                'label': 'hui'
            }),
            'login': TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Введите логин'
            }),
            'password': PasswordInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Введите пароль'
            })
        }
