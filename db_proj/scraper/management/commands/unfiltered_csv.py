import sys

from scraper.models import *
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

sys.path.insert(1, 'scraper/data/')
from school_dept import data

class Command(BaseCommand):
	help = """Takes a csv file (without rows x columns) and converts it to db objects based on what we've got."""


	# Our data set is in the form 
	#[[(school1 name, school1 url), (department1 name, department1 url), ....] , 
	# [(school2 name, school2 url), (department1 name, department1 url), ....] , 
	#   ...
	# ]
	def handle(self, *kwargs, **options):
		for large_arr in data:
			school = School(name=large_arr[0][0], url=large_arr[0][1])
			school.save()
			for tup in large_arr[1::]:
				Department(name=tup[0], url=tup[1], school=school).save()
			
