from scraper.models import *
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

class Command(BaseCommand):
	help = """Populate our database with default objects for each model"""


	def handle(self, *kwargs, **options):
		s = School(name='DEFAULT')
		d = Department(name='DEFAULT', school=s)
		i = Instructor(case_id='DEFAULT', name='DEFAULT', dept=d)
		c = Course(course_id='DEFAULT', dept=d, units=3, name='DEFAULT', instructor=i)
		r = Review(description='DEFAULT DEFAULT DESC', course=c)
		se = Section(section_num=101, course=c)
		
		s.save()
		d.save()
		i.save()
		c.save()
		r.save()
		se.save()