from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views import generic
from django.db.models import Q
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView

import re

from .forms import NewUserForm
from .models import *

# It'd probably be a good goal to display all of the info that we can get in our db in some way...

# infinite scroll for data display on search
# https://simpleisbetterthancomplex.com/tutorial/2017/03/13/how-to-create-infinite-scroll-with-django.html

class CreateUser(CreateView):
	model = Profile
	fields = '__all__'
	template_name = 'scraper/form.html'

	def form_valid(self, form):
		self.object = form.save()
		return HttpResponseRedirect('/', '/')


class SearchView(generic.TemplateView):
	template_name = 'scraper/search.html'
	
	# Rewrite this to just be a search that calls a query to generate the product list view
	# Just gonna use the template as a form rather than making one in forms.py

# expand on this by using the bottom part of:
# https://wsvincent.com/django-search/
# to create a form that will add slugs based on what we want
class CourseListView(generic.ListView):
	template_name = 'scraper/courses.html'

	def get_queryset(self):
		query = self.request.GET
		# Expected values to return:
		# cname, cin, dept, in, hr all as string direct map to model for Course
		print(query)
		return Course.objects.all()
		# try:
		# 	# Apply a regex to determine what type of search we're getting on course info:
		# 	search_terms = re.compile("^[a-zA-Z]{3,4}\\s*[0-9]{3}").findall(search_query)
		# 	if search_terms:
		# 		return Course.objects.filter(course_id__icontains=search_terms[0])
		# 	# Otherwise, check course title for all of the items in query
		# 	else:
		# 		return Course.objects.filter(name__icontains=search_query)
		# 	pass
		# except:
		# 	return Course.objects.all()


class UserView(generic.ListView):
	template_name = 'scraper/base.html'

	def get_queryset(self):
		# Ideally get a user's set of favorites.
		pass


	# Incase we need it...
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		# If we can't find the mentioned user, 404
		# context['user'] = get_object_or_404(User, ..)
		return context	


class DepartmentView(generic.ListView):
	template_name = 'scraper/base.html'

	# Add something to the slug to get all of the units in here
	def get_queryset(self):
		return Department.objects.all()


class InstructorView(generic.ListView):
	template_name = 'scraper/base.html'

	# Do similar thing to Dept.View
	def get_queryset(self):
		return Instructor.objects.all()

