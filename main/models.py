from django.db import models
from datetime import datetime

class ItemCategory(models.Model):
	item_category = models.CharField(max_length=200, default=1)
	category_summary = models.CharField(max_length=200)
	category_slug = models.CharField(max_length=200, default=1)

	class Meta:
		verbose_name_plural = "Categories"

	def __str__(self):
		return self.item_category	

class ItemSeries(models.Model):
	item_series = models.CharField(max_length=200, default=1)
	item_category = models.ForeignKey(ItemCategory, verbose_name= "Category", default=1,  on_delete=models.SET_DEFAULT)
	series_summary = models.CharField(max_length=200)

	class Meta:
		verbose_name_plural = "Series"

	def __str__(self):
		return self.item_series	

def upload_location(instance, filename):
    filebase, extension = filename.split('.')
    return 'item_image/%s.%s' % (instance.item_name, extension)

class Item(models.Model):

	item_name = models.CharField(max_length = 200)
	item_discription = models.TextField()
	item_update = models.DateTimeField("Last Updated", default = datetime.now(), blank=True, null=True)						   
	temp = "item_image/"+str(item_name)+".jpg"
	item_img = models.ImageField(upload_to=upload_location, blank=True, null=True)	

	item_series = models.ForeignKey(ItemSeries, verbose_name= "Series", default=1,  on_delete=models.SET_DEFAULT)
	item_slug = models.CharField(max_length=200, default=1)

	def __str__(self):
		return self.item_name


# default=1,  on_delete=models.SET_DEFAULT