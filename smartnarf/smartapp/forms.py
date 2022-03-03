#from .models import User
from django.forms import ModelForm, TextInput, CharField, PasswordInput, ModelChoiceField
from django.contrib.auth.forms import UserCreationForm
from authentication.models import User
from .models import Group


class NewUserForm(UserCreationForm):
	#group = ModelChoiceField(queryset=Group.objects.all(), label='Huisosi')

	class Meta:
		model = User
		fields = ("username", "group", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)

		if commit:
			user.save()
		return user
