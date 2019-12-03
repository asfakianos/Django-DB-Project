# from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView, FormMixin
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

import re

from .forms import *
from .models import *

# We need to check dictionary key existence before we attempt to do anything...
# If it doesn't exist, let's just create and fill it with a default value ('' or 0)

# It'd probably be a good goal to display all of the info that we can get in our db in some way...

# infinite scroll for data display on search
# https://simpleisbetterthancomplex.com/tutorial/2017/03/13/how-to-create-infinite-scroll-with-django.html

# We can make this for all the objects
class CreateUser(CreateView):
	model = Profile
	fields = '__all__'
	template_name = 'scraper/form.html'

	def form_valid(self, form):
		self.object = form.save()
		return HttpResponseRedirect('/', '/')


# Nothing really so see here
class SearchView(TemplateView):
	template_name = 'scraper/search.html'
	

# expand on this by using the bottom part of:
# https://wsvincent.com/django-search/
# to create a form that will add slugs based on what we want
class CourseListView(ListView):
	template_name = 'scraper/courses.html'

	def get_queryset(self):
		query = self.request.GET
		# Expected values to return:
		# 'cname': name, 'course_id': course_id, 'units': units, 'instructor': instructor, 'dept': dept
		print(query)
		# This is the current issue. You can't set it to 0 if there's nothing there
		if query['units'] != '':
			return Course.objects.filter(course_id__icontains=query['course_id'], 
										 units=int(query['units']),
										 name__icontains=query['cname'],
										 instructor__name__icontains=query['instructor'],
										 dept__name__icontains=query['dept']
										)

		else:
			return Course.objects.filter(course_id__icontains=query['course_id'], 
							 name__icontains=query['cname'],
							 instructor__name__icontains=query['instructor'],
							 dept__name__icontains=query['dept']
							)


# TOADD:
# Time conflict notification on course watch list
class UserView(ListView):
	# TODO
	template_name = 'scraper/base.html'

	def get_queryset(self):
		query = self.request.GET

		# Not ideal, but demonstrates the query exists
		# We can handle a non-existent query set in the template view
		if 'user_id' in query:
			return Profile.objects.get(id=query['user_id'])
		
	# Incase we need it...
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		# If we can't find the mentioned user, 404
		# context['user'] = get_object_or_404(User, ..)
		return context	


class DepartmentView(ListView):
	# TODO
	template_name = 'scraper/base.html'

	# Add something to the slug to get all of the units in here
	def get_queryset(self):
		query = self.request.GET
		# Get all courses in this dept or all courses not in this dept.
		# ?in, ?not_in, or both -- NOT BOTH as we either get everything in a dept or everything not in a dept...the intersect is just the in
		# if 'in' in query and 'not_in' in query:
		# 	return 

		if 'in' in query:
			return Course.objects.filter(dept__name__icontains=query['in'])

		elif 'not_in' in query:
			return Course.objects.exclude(dept__name__icontains=query['not_in'])

		# Note that nothing gets returned if we don't have anything in the GET request.
		# If we want to get 

			# return Department.objects.filter(name__icontains=query['dept'])


class InstructorView(ListView):
	# TODO
	template_name = 'scraper/base.html'

	# Do similar thing to Dept.View
	def get_queryset(self):
		query = self.request.GET

		# Expected; ?prof=PROFESSOR
		try:
			if 'prof' in query:
				return Instructor.objects.get(name__icontains=query['prof'])

			# Equivalent of ?id=ID
			elif 'id' in query:
				return Instructor.objects.get(case_id=query['id'])

		except Instructor.DoesNotExist:
			pass


# Form for writing/submitting reviews
# Render a form as well as class info.
class CourseView(ListView, FormMixin):
	template_name='scraper/base.html'
	form_class = CourseReviewForm

	def get_queryset(self):
		return Review.objects.all()

	def get_context_data(self, *args, **kwargs):
		context = super(CourseView, self).get_context_data(*args, **kwargs)
		context['slug'] = self.kwargs['slug'] # Use this to find specific user
		print(Course.objects.filter(course_id=context['slug']))
		return context


class CustomView(ListView):
	template_name='scraper/courses.html'

	def get_queryset(self):
		query = self.request.GET
		print(query['query']) # DEBUG
		# Our query set should be received from raw sql!!!
		sql_query = "SELECT course_id, units, name " + self._prepare_sql_query(query['query'])
		print(sql_query)
		return Course.objects.raw(sql_query)


	def _prepare_sql_query(self, base_query):
		# We have to replace all of these instances with "scraper_lowercaseversion"
		regex_list = ['(?i)course[a-zA-Z|\\s]', '(?i)instructor[a-zA-Z|\\s]', 
					  '(?i)department[a-zA-Z|\\s]', '(?i)school[a-zA-Z|\\s]', 
					  '(?i)section[a-zA-Z|\\s]', '(?i)review[a-zA-Z|\\s]']
		table_list = ['scraper_course', 'scraper_instructor', 'scraper_department', 
					  'scraper_school', 'scraper_section', 'scraper_review']

		for i in range(len(regex_list)):
			base_query = re.sub(regex_list[i], table_list[i], base_query)

		return base_query

