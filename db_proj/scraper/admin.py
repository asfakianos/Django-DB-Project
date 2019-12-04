from django.contrib import admin
from .models import *


admin.site.register(Course)
admin.site.register(Instructor)
admin.site.register(Department)
admin.site.register(School)
admin.site.register(Section)
admin.site.register(Profile)
admin.site.register(Review)