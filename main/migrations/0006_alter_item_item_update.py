# Generated by Django 3.2.3 on 2021-06-10 12:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_item_item_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_update',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 10, 18, 0, 29, 310807), null=True, verbose_name='Last Updated'),
        ),
    ]