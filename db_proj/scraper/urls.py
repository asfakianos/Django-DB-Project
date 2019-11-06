from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	# path('products', views.ProductListView.as_view(), name='results'),
	# path('product/<slug:product_name>', views.product_page, name='product-page'),
	# path('user/<slug:')
]
