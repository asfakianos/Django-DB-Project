from django.db import models


# We'll make models here, and have a separate module that populates dbs when necessary
# Model for each item that we'd feature
class Course(models.Model):
	course_id # CharField, pkey
	prereqs # Foreign Key, can be removed if too difficult/finicky
	dept # Foreign Key
	units # Foreign Key
	name # CharField

# It doesn't look like we can get the courses taught be this professor
class Instructor(models.Model):
	name # CharField
	dept #CharField

class Department(models.Model):
	name # CharField
	address #CharField
	school #ForeignKey

class School(models.Model):
	name #CharField

# class Student(models.Model):
# probably modified user model