# Generated by Django 3.2.3 on 2021-06-16 13:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20210616_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_update',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 16, 19, 8, 45, 469719), null=True, verbose_name='Last Updated'),
        ),
    ]
