from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('product/<slug:product_name>', views.product_page, name='product-page')
]
