from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.conf import settings
from . import models

class NewUserForm(forms.Form):
	# Fields here...
	some_field = forms.CharField(max_length=20)

	def clean(self):
		cleaned_data = super().clean()
		# field = cleaned_data.get('field')
		# if...
		# else raise validationerror


class CourseReviewForm(forms.Form):
	Review = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'form': 'review_form'}))

	def clean(self):
		cleaned_data = super().clean()
		print(cleaned_data)

		# Eventually:
		# Review.objects new