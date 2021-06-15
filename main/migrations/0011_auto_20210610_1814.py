# Generated by Django 3.2.3 on 2021-06-10 12:44

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20210610_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_series',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.itemseries', verbose_name='Series'),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_update',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 10, 18, 14, 18, 474158), null=True, verbose_name='Last Updated'),
        ),
    ]
