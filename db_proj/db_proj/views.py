from django.shortcuts import redirect, render
from django.template import RequestContext
from django.db import models
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout, login, authenticate

from scraper.models import *


def logout_redirect(request):
	logout(request)
	return HttpResponseRedirect('/')


def create_redirect_view(request):
	response = request.POST
	# Create a user 
	# .get each attribute from here to create a User.
	if request.method == 'POST':
		form = NewUserForm(request.POST)
		if form.is_valid():
			print(request.POST)
			# https://stackoverflow.com/questions/35796195/how-to-redirect-to-previous-page-in-django-after-post-request/35796330
			return HttpResponseRedirect(response.get('/', '/'))

	else:
		form = NewUserForm()
	
	return render(request, 'scraper/login.html', {'form': form})


def login_user(request):
	logout(request)
	context = {}
	if request.POST:
		username = request.POST['username']
		password = request.POST['password']

	    # Means we are making a new user
		if 'confirm_password' in request.POST:
	    	# We're also not catching duplicate usernames or anything...
			if request.POST['confirm_password'] == password:
				user = User.objects.create_user(username=username,
					                                password=password)
		        # We should do something about this, but I'm going to let it slide.
			else:
				return HttpResponseRedirect('login/')


		user = authenticate(username=username, password=password)
		# Then check if profile is defined for this user, otherwise make one
		if user is not None:
			try:
				profile = Profile.objects.get(user__username=user.username)
			except:
				profile = Profile.objects.create(user=user)
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/')
	return render(request, 'scraper/login.html', context)

