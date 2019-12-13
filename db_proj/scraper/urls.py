from django.urls import path, re_path

from .views import *

urlpatterns = [
	path('', SearchView.as_view(), name='index'),
	path('courses/', CourseListView.as_view(), name='course_search'),
	path('course/<slug:slug>', CourseView.as_view(), name='course_page'),
	path('submit_review/', submit_review, name='submit_review'),
	path('watch_course/', watch_course, name='watch_course'),
	path('dept/', DepartmentView.as_view(), name='dept'),
	path('instructor/', InstructorView.as_view(), name='instructor'),
	path('customsearch/', CustomView.as_view(), name='custom_sql'),
	path('user/', UserView.as_view(), name='user'),
]
