# Generated by Django 3.0.7 on 2020-07-01 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='slug',
            field=models.SlugField(default='TFpI53FuTevVjzqeJbeqNMLStMyuD3CZBQp5b3SGU13r39mg8UI7nLCgVsRDKo46b9BSWCCWS8kM9MUSlarqw2pXS5', max_length=250, unique=True, unique_for_date='publish'),
        ),
        migrations.AlterField(
            model_name='story',
            name='story',
            field=models.FileField(upload_to='stories/%Y/%m/%d'),
        ),
    ]
