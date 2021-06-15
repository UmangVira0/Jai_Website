from django.contrib import admin
from .models import Item, ItemSeries, ItemCategory
from django.db import models

class ItemAdmin(admin.ModelAdmin):
	fieldsets = [
		("Title/date", {"fields": ["item_name", "item_update"]}),
		("URL", {"fields": ["item_slug"]}),
		("Series", {"fields": ["item_series"]}),
		("Content", {"fields": ["item_discription"]})
	]


admin.site.register(ItemSeries)
admin.site.register(ItemCategory)
admin.site.register(Item, ItemAdmin)