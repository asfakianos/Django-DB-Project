from django.urls import path

from .views import *

urlpatterns = [
	path('', SearchView.as_view(), name='index'),
	path('courses/', CourseListView.as_view(), name='course_search'),
	path('dept/<slug:dept_name>', DepartmentView.as_view(), name='dept'),
	path('instructor/<slug:teacher_name>', InstructorView.as_view(), name='instructor'),
	# path('products', views.ProductListView.as_view(), name='results'),
	# path('product/<slug:search_query>', views.product_page, name='product-page'),
]
