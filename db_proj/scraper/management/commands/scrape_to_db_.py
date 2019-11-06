import beautifulsoup4
import requests

from scraper.models import *
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.conf import settings

class Command(BaseCommand):
	help = """Scrape all data that we need for our models from the case website and write it to the appropriate models."""

	def _scrape_from_site(self):
		pass