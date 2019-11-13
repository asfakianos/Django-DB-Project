from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def validate_credit_hours(n):
	# The only case I found where the hours are outside of this range are for EECS600 (1-18)
	if n < 1 or n > 4:
		raise ValidationError(
			('%(n)s is not a usual number of credit hours'),
			params={'value': n})


# We'll make models here, and have a separate module that populates dbs when necessary
# Model for each item that we'd feature
class Course(models.Model):
	course_id = models.CharField(max_length=10, primary_key=True) # CharField, pkey
	# prereqs = models.ForeignKey(# Foreign Key, can be removed if too difficult/finicky
	dept = models.ForeignKey(
		'Department',
		on_delete=models.PROTECT # We don't want to lose a department since we know every class has a dpt.
	)
	units = models.IntegerField(validators=[validate_credit_hours]) # Look into Min/MaxValueValidators for this
	name = models.CharField(max_length=100)
	instructor = models.ForeignKey(
		'Instructor',
		null=True,
		on_delete = models.SET_NULL
	)


# It doesn't look like we can get the courses taught be this professor
# Needs it for all, but sample @ https://artsci.case.edu/about-the-college/faculty-directory/
class Instructor(models.Model):
	name = models.CharField(max_length=30)
	dept = models.ForeignKey(
		'Department',
		null=True,
		on_delete = models.SET_NULL
	)
	title = models.CharField(max_length=30)
	# I'm not entirely sure how long these can be. Obviously, ours are 5-6 chars, but if we can't find those for all teachers, we'll end up using their first.last
	email_id = models.CharField(max_length=20, primary_key=True)


class Department(models.Model):
	# I don't think there are any duplicate dept names, but if there is then we can adjust this to not be pk
	name = models.CharField(max_length=50, primary_key=True)
	address = models.CharField(max_length=50)
	school = models.ForeignKey(
		'School',
		null=True,
		on_delete = models.SET_NULL)


class School(models.Model):
	# Same logic as Departments
	name = models.CharField(max_length=50, primary_key=True)


# Extension of user model to build on favorites of classes, etc.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	watched_classes = models.ManyToManyField('Course')
