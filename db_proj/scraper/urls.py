from django.urls import path, re_path

from .views import *

urlpatterns = [
	path('', SearchView.as_view(), name='index'),
	path('courses/', CourseListView.as_view(), name='course_search'),
	# Idk wtf is happening here
	path(r'^course/[\w]+/$', CourseView.as_view(), name='course_page'),
	path(r'^course/[\w]+/submit_review/$', submit_review, name='submit_review'),
	path('dept/', DepartmentView.as_view(), name='dept'),
	path('instructor/', InstructorView.as_view(), name='instructor'),
	path('customsearch/', CustomView.as_view(), name='custom_sql'),
]
