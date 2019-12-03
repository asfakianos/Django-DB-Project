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
		# Create the dictionary mapping for class code to Department
		class_mapping = pd.read_csv(DICT_PATH)
		class_mapping = dict(zip(list(class_mapping['CODE']), list(class_mapping['TITLE'])))

		# Now parse the data!
		csv = pd.read_csv(FILE_PATH)

		for index, row in csv.iterrows():
			try:
				dept = Department.objects.filter(name__icontains=class_mapping[row['department']])[0]
			except:
				# print("RIP", row['department'], '=', class_mapping[row['department']])
				dept = Department.objects.filter(name__icontains='DEFAULT')[0]

			# Find instructor, and make if not exists
			try:
				instructor = Instructor.objects.filter(name=row['instructor'], dept=dept)[0]
			except:
				instructor = Instructor(name=row['instructor'], dept=dept, case_id=len(Instructor.objects.all()) + 1)
				instructor.save()


			# Check if course exists, then add instructor to it?
			new_course = Course(course_id=row['department'] + row['Course_id'], dept=dept, instructor=instructor, units=row['units'], name=row['name'])
			new_course.save()
			# Just to show we support to Section functionality..
			num_similar =  len(Course.objects.filter(name__icontains=new_course.name, course_id__icontains=new_course.course_id))
			# We don't have meeting times yet.
			new_section = Section(section_num=num_similar + 100, course=new_course)
			new_section.save()

			transaction.commit()


