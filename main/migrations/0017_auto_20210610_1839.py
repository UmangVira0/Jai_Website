# Generated by Django 3.2.3 on 2021-06-10 13:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20210610_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_update',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 10, 18, 39, 7, 555656), null=True, verbose_name='Last Updated'),
        ),
        migrations.AlterField(
            model_name='itemseries',
            name='item_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.itemcategory', verbose_name='Category'),
        ),
    ]
