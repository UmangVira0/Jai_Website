from django.db import models
from datetime import datetime
# Create your models here.
class Item(models.Model):
	item_name = models.CharField(max_length = 200)
	item_discription = models.TextField()
	item_update = models.DateTimeField("Last Updated",
									   default = datetime.now(),
									   blank=True, 
									   null=True)


	def __str__(self):
		return self.item_name
