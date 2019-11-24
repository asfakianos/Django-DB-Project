from scraper.models import *
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

class Command(BaseCommand):
	help = """Populate our database with default objects for each model"""


	def handle(self, *kwargs, **options):
		s = School(name='DEFAULT')
		s.save()
		d = Department(name='DEFAULT', address='NONE', school=s)
		d.save()
		i = Instructor(case_id='DEFAULT', name='DEFAULT', dept=d)
		i.save()
		c = Course(course_id='DEFAULT', dept=d, units=3, name='DEFAULT', instructor=i)
		c.save()