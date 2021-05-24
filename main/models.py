from django.db import models

# Create your models here.
class Item(models.Model):
	item_name = models.CharField(max_length = 200)
	item_discription = models.TextField()

	def __str__(self):
		return self.item_name
