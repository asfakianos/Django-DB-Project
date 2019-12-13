from scraper.models import *
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.db import transaction

import pandas as pd

# Specify this path from the db_proj directory (where manage.py is located)
FILE_PATH="scraper/data/prof_with_meeting_times.csv"

class Command(BaseCommand):
	help = """Takes a csv from FILE_PATH and modifies all instructors in the list to match the review given"""

	def handle(self, *kwargs, **options):
		i = Instructor.objects.all()
		csv = pd.read_csv(FILE_PATH)

		prof_to_rating = dict(zip(list(csv['instructor']), list(csv['rating'])))
		for name in prof_to_rating:
			print(name, prof_to_rating[name])
			try: 
				for target in i.filter(name__iexact=name):
					target.rating = prof_to_rating[name]
					target.save()
			except:
				pass

