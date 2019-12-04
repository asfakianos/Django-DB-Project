from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def validate_credit_hours(n):
	# The only case I found where the hours are outside of this range are for EECS600 (1-18)
	if n < 1 or n > 20:
		raise ValidationError(
			('%(n)s is not a usual number of credit hours'),
			params={'value': n})


DEFAULT_INST = 'DEFAULT'
DEFAULT_DEPT = 'DEFAULT'
DEFAULT_SCHL = 'DEFAULT'
# DEFAULT_USER = '------'

# We'll make models here, and have a separate module that populates dbs when necessary
# Model for each item that we'd feature
class Course(models.Model):
	course_id = models.CharField(max_length=10, primary_key=True) # CharField, pkey
	# prereqs = models.ForeignKey(# Foreign Key, can be removed if too difficult/finicky
	dept = models.ForeignKey(
		'Department',
		default=DEFAULT_DEPT,
		on_delete=models.SET_DEFAULT
	)
	units = models.IntegerField(validators=[validate_credit_hours]) # Look into Min/MaxValueValidators for this
	name = models.CharField(max_length=100)
	instructor = models.ForeignKey(
		'Instructor',
		default=DEFAULT_INST,
		on_delete=models.SET_DEFAULT
	)

	def __str__(self):
		return f"{self.course_id} - {self.name}"


# It doesn't look like we can get the courses taught be this professor
# Needs it for all, but sample @ https://artsci.case.edu/about-the-college/faculty-directory/
class Instructor(models.Model):
	# Assuming we can get it, I think the max length is 6, but 10 for safety
	case_id = models.CharField(max_length=10, primary_key=True, default=DEFAULT_INST)
	name = models.CharField(max_length=30, default=DEFAULT_INST) #primary_key=True,
	dept = models.ForeignKey(
		'Department',
		default=DEFAULT_DEPT,
		on_delete=models.SET_DEFAULT
	)
	rating = models.DecimalField(default=5.0, max_digits=3, decimal_places=2)

	def __str__(self):
		return f"{self.case_id} {self.name} from {self.dept.name}"
	# Potentially add RateMyProfessor as a separate model or in this.
	# Once data is added to this, then Phil can go back through and automate case_id for instructors. 
	# I'm not entirely sure how long these can be. Obviously, ours are 5-6 chars, but if we can't find those for all teachers, we'll end up using their first.last


class Department(models.Model):
	# I don't think there are any duplicate dept names, but if there is then we can adjust this to not be pk
	name = models.CharField(max_length=50, primary_key=True, default=DEFAULT_DEPT)
	url = models.CharField(max_length=100, default="https://case.edu/bulletin/")
	school = models.ForeignKey(
		'School',
		default=DEFAULT_SCHL,
		on_delete=models.SET_DEFAULT
		)

	def __str__(self):
		return f"{self.name}"


class School(models.Model):
	# Same logic as Departments
	name = models.CharField(max_length=50, primary_key=True, default=DEFAULT_SCHL)
	url = models.CharField(max_length=100, default="https://case.edu/bulletin/")

	def __str__(self):
		return self.name


# Extension of user model to build on favorites of classes, etc.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	watched_classes = models.ManyToManyField('Course')


# A course can have one or multiple sections
class Section(models.Model):
	section_num = models.IntegerField(default=100)
	meeting_times = models.CharField(max_length=30, null=True)
	course = models.ForeignKey(
		'Course',
		on_delete=models.CASCADE
		)


class Review(models.Model):
	description = models.TextField()
	added_at = models.DateTimeField('Created time', auto_now_add=True, null=True)
	course = models.ForeignKey(
		'Course',
		on_delete=models.CASCADE
		)


