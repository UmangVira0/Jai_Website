# Generated by Django 3.2.3 on 2021-06-16 13:18

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_alter_item_item_update'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_img',
            field=models.ImageField(blank=True, null=True, upload_to='item_image/<django.db.models.fields.CharField>.jpg'),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_series',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.itemseries', verbose_name='Series'),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_update',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 16, 18, 48, 25, 505913), null=True, verbose_name='Last Updated'),
        ),
        migrations.AlterField(
            model_name='itemcategory',
            name='item_category',
            field=models.CharField(default=1, max_length=200),
        ),
        migrations.AlterField(
            model_name='itemseries',
            name='item_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.itemcategory', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='itemseries',
            name='item_series',
            field=models.CharField(default=1, max_length=200),
        ),
    ]