# Generated by Django 3.0.7 on 2020-06-24 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0013_auto_20200624_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='slug',
            field=models.SlugField(default='BPXCB6PChyIWxdFRRvP0', max_length=250, unique=True, unique_for_date='publish'),
        ),
    ]
