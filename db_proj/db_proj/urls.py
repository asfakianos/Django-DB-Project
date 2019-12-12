from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView
from django.conf import settings

# from .views import *
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_user, name='login'),
    path('', include('scraper.urls')),
	path('logout/', views.logout_redirect, name='logout'),
]


