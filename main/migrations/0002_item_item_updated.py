# Generated by Django 3.2.3 on 2021-05-24 12:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_updated',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Last Updated'),
            preserve_default=False,
        ),
    ]