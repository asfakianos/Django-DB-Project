import beautifulsoup4
import requests

from scraper.models import *
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

class Command(BaseCommand):
	help = """Scrape all data that we need for our models from the case website and write it to the appropriate models."""

	def _scrape_from_site(self):
		pass

	# If we have any optional arguments to add, put them here.
	def add_arguments(self, parser):
		pass
		# e.g.
		# parser.add_argument('--NAME', action='ACTION', help='HELP_TEXT')


	def handle(self, *kwargs, **options):
		data = self._scrape_from_site()
		# Add data to existing models if they don't exist already
		# Objects.add(DATA)