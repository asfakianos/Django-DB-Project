from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.conf import settings
from .models import *

class NewUserForm(forms.Form):
	# Fields here...
	some_field = forms.CharField(max_length=20)

	def clean(self):
		cleaned_data = super().clean()
		# field = cleaned_data.get('field')
		# if...
		# else raise validationerror
