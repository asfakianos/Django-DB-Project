from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Item

# Create your views here.
def index(request):
	return HttpResponse("Home.")

def product_page(request, name):
	try:
		item = Items.objects.get(name=name)
		print("Issue with finding object with name {}", name)
	except:
		all_items = Items.objects.all()
		for i in all_items:
			if i.contains(name):
				item = i
				break
	return HttpResponse("E")
