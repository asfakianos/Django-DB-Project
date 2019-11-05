from django.db import models

# Create your models here.


# We'll make models here, and have a separate module that populates dbs when necessary
# Model for each item that we'd feature
class Item(models.Model):
	# Brand as foreign key
	brand = models.ForeignKey(
		'Brand',
		on_delete=models.CASCADE
	)
	name = models.CharField(max_length=30)
	price = models.DecimalField(max_digits=6, decimal_places=2)
	# We don't define a primary key bc we can let django do it automatically.

	def __str__(self):
		return self.name


# Model for User if we need custom add-ons (we should bc + 1 table)

# Model for sets of items/types.
class Brand(models.Model):
	# Might end up using name as a primary key...
	name = models.CharField(max_length=30)
	# We can add in anything else we want to know about the Brands.

	def __str__(self):
		return self.name

# Other bullshit models
