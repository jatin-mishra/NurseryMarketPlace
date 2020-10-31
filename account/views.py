from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required



# Create your views here.
def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}')
			return redirect('login')
		# else:
		# 	messages.error(request, f'form invalid')
		# 	return redirect('plant-home')
	else:
		form = UserRegisterForm()
	return render(request, 'account/register.html', { 'form' : form })

@login_required
def profile(request):
	if request.method == 'POST':
		form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
		if form.is_valid():
			form.save()
			messages.success(request, f'{ request.user.username }!, your account has been updated')
			return redirect('profile')
	else:
		form = UserUpdateForm(instance=request.user)

	return render(request, 'account/profile.html', { 'form' : form })