from django.shortcuts import render
from django.http import HttpResponse
# from django.contrib.auth.decorators import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views import generic

from .models import Item, Brand

# Create your views here.
def index(request):
	return HttpResponse("Home.")

def product_page(request, product_name):
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


# See https://github.com/CWRU-Connected-Devices/connected-devices-spring19/blob/master/Web/lampisite/lampi/templates/lampi/index.html
# for dynamic page based on models loaded
# We obviously don't need login here, but if we have it we want to work with it...
class ProductListView(generic.ListView):
	template_name = 'scraper/index.html'

	def get_queryset(self):
		# Return some set of results filtered from Item
		# e.g.
		# return Item.objects.filter(id=1)
		# can also be a list.
		# We'd want to update this based on what a user is interested in (potentially add favorites down the road)
		pass

