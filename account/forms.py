from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):

	email = forms.EmailField(max_length=60, required=True, widget=forms.TextInput(attrs={'placeholder':'Email'}))
	is_manager = forms.BooleanField(required=False)

	class Meta:
		model = get_user_model()
		fields = ['username', 'email','password1','password2', 'is_manager']



class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField(max_length=60, required=True, widget=forms.TextInput(attrs={'placeholder':'Email'}))
	is_manager = forms.BooleanField(required=False)
	profile_pic = forms.ImageField()

	class Meta:
		model = get_user_model()
		fields = ['username', 'email', 'is_manager', 'profile_pic']
