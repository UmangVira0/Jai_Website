from django.contrib import admin
from .models import Item
from django.db import models

class ItemAdmin(admin.ModelAdmin):
	fieldsets = [
		("Title/date", {"fields": ["item_name", "item_update"]}),
		("Content", {"fields": ["item_discription"]})
	]

admin.site.register(Item, ItemAdmin)