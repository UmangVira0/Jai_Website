# Generated by Django 3.2.3 on 2021-06-10 12:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20210610_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_update',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 10, 18, 8, 59, 563879), null=True, verbose_name='Last Updated'),
        ),
        migrations.AlterField(
            model_name='itemcategory',
            name='category_slug',
            field=models.CharField(default=1, max_length=200),
        ),
    ]
