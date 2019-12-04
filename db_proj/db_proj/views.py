from django.shortcuts import redirect, render
from scraper.forms import NewUserForm
from scraper.models import *
from django.db import models
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.contrib.auth import logout


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

	