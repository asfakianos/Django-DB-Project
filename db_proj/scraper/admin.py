from django.contrib import admin
from .models import *

# Register your models here.
# class CourseAdmin(admin.ModelAdmin):
# 	list_display = ('course_id', 'units', 'name', 'instructor', 'dept')

admin.site.register(Course)