from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views import generic

from .models import Item, Brand#, User

# It'd probably be a good goal to display all of the info that we can get in our db in some way...


# Create your views here.
def index(request):
	return HttpResponse("Hello.")
	# Rewrite this to just be a search that calls a query to generate the product list view


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
class CourseListView(generic.ListView):
	template_name = 'scraper/products.html'

	def get_queryset(self):
		# Return some set of results filtered from Item
		# e.g.
		# return Item.objects.filter(id=1)
		# can also be a list.
		# We'd want to update this based on what a user is interested in (potentially add favorites down the road)
		pass


class UserView(generic.ListView):
	template_name = ''

	def get_queryset(self):
		# Ideally get a user's set of favorites.
		pass


	# Incase we need it...
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		# If we can't find the mentioned user, 404
		# context['user'] = get_object_or_404(User, ..)
		return context	