from scraper.models import *
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.db import transaction

import pandas as pd

# Specify this path from the db_proj directory (where manage.py is located)
FILE_PATH="scraper/data/________"

class Command(BaseCommand):
	help = """Takes a csv from FILE_PATH and modifies all instructors in the list to match the review given"""

	def handle(self, *kwargs, **options):
		i = Instructor.objects.all()
		ratings = pd.read_csv(FILE_PATH)

		for index, row in ratings.interrows():
			target = i.get(name__iexact=row['name'])
			target.rating = row['rating']
			target.save()

