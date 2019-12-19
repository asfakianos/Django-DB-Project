from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic.edit import CreateView, FormMixin
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

import re
import json

from .forms import *
from .models import *


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

	def post(self, request):
		pass


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


class UserView(ListView):
	template_name = 'scraper/user_view.html'

	def get_queryset(self):
		query = self.request.GET
		# Not ideal, but demonstrates the query exists
		# We can handle a non-existent query set in the template view
		if 'username' in query:
			profile = Profile.objects.get(user__username__iexact=query['username'])
			return profile.watched_classes.all()
		
	# Not going to handle invalid users
	def get_context_data(self, **kwargs):
		query = self.request.GET
		context = super().get_context_data(**kwargs)
		context['user'] = Profile.objects.get(user__username__iexact=query['username']).user
		return context	


class DepartmentView(ListView):
	# TODO
	template_name = 'scraper/base.html'

	# Add something to the slug to get all of the units in here
	def get_queryset(self):
		query = self.request.GET
		if 'in' in query:
			return Course.objects.filter(dept__name__icontains=query['in'])

		elif 'not_in' in query:
			return Course.objects.exclude(dept__name__icontains=query['not_in'])


class InstructorView(ListView):
	template_name = 'scraper/instructor_view.html'

	# Do similar thing to Dept.View
	def get_context_data(self, **kwargs):
		query = self.request.GET
		context = super().get_context_data(**kwargs)

		# Expected; ?prof=PROFESSOR
		try:
			if 'prof' in query:
				context['instructor'] = Instructor.objects.get(name__iexact=query['prof'])

			# Equivalent of ?id=ID
			elif 'id' in query:
				context['instructor'] = Instructor.objects.get(case_id__iexact=query['id'])

		except:
			pass

		return context


	def get_queryset(self):
		query = self.request.GET
		try:
			if 'prof' in query:
				instructor = Instructor.objects.get(name__iexact=query['prof'])

			# Equivalent of ?id=ID
			elif 'id' in query:
				instructor = Instructor.objects.get(case_id__iexact=query['id'])

			return Course.objects.filter(instructor=instructor)

		except Instructor.DoesNotExist:
			pass



# Form for writing/submitting reviews
# Render a form as well as class info.
class CourseView(ListView, SingleObjectMixin):
	template_name='scraper/course_view.html'
	form_class = CourseReviewForm


	def get_context_data(self, **kwargs):
		# I couldn't get request to work, and this is basically all I wanted
		path_re = re.compile('[\\w]+$')
		course_id = path_re.findall(self.request.path)[0]
		reviews = Review.objects.filter(course__course_id__icontains=course_id)

		# Add neccessary stuff to our context
		context = {}
		context['course'] = Course.objects.get(course_id=self.kwargs['slug'])
		context['form'] = CourseReviewForm()
		context['review_list'] = reviews
		return context


	def get_queryset(self, **kwargs):
		return Review.objects.filter(course__course_id=Course.objects.get(course_id=self.kwargs['slug']).course_id)		


class CustomView(ListView):
	template_name='scraper/courses.html'

	def get_queryset(self):
		query = self.request.GET
		try:
			sql_query = self._prepare_sql_query(query['query'])
			return Course.objects.raw(sql_query)
		except:
			return Course.objects.raw("SELECT * FROM scraper_course")
		


	# Likely just going to let this through and assume the user inputs proper sql
	def _prepare_sql_query(self, base_query):

		return base_query


def submit_review(request):
	review = request.POST.get('review')
	course_id = request.POST.get('course')
	new_review = Review.objects.create(description=review, 
								course=Course.objects.get(course_id__icontains=course_id))

	new_review.save()
	return JsonResponse({"review":new_review.description})


def watch_course(request):
	username = request.POST.get('username')
	course_id = request.POST.get('course')

	profile = Profile.objects.filter(user__username__icontains=username)[0]
	if Course.objects.get(course_id__iexact=course_id) in profile.watched_classes.all():
		return JsonResponse({"status":"duplicate"})

	profile.watched_classes.add(Course.objects.get(course_id__iexact=course_id))
	profile.save()

	return JsonResponse({"status":"OK"})

