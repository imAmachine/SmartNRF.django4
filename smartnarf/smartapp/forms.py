#from .models import User
from django.forms import ModelForm, TextInput, CharField, PasswordInput


# class UserRegisterForm(ModelForm):
#     password2 = CharField(label='password2', widget=PasswordInput(attrs={
#                 'class': 'form-control mb-2',
#                 'placeholder': 'Повторите пароль'
#             }))
#
#     class Meta:
#         model = User
#         fields = ['username', 'password']
#
#         widgets = {
#             'username': TextInput(attrs={
#                 'class': 'form-control mb-2',
#                 'placeholder': 'Введите имя',
#                 'label': 'hui'
#             }),
#             'password': PasswordInput(attrs={
#                 'class': 'form-control mb-2',
#                 'placeholder': 'Введите пароль'
#             })
#         }
