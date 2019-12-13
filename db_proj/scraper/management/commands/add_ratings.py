from scraper.models import *
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.db import transaction

import pandas as pd

FILE_PATH="scraper/data/dbproj_sample1.csv"
DICT_PATH="scraper/data/course_dict.csv"


class Command(BaseCommand):
	help = """Takes a csv file (must have actual rows x columns) and converts it to db objects based on what we've got."""

	def handle(self, *kwargs, **options):
		