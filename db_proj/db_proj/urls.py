from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView
from django.conf import settings

# from .views import *
from . import views


# template_name='scraper/login.html'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('', include('scraper.urls')),
	path('logout/', views.logout_redirect, name='logout'),
]


