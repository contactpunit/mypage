# Generated by Django 3.0.7 on 2020-06-29 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0013_auto_20200629_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='slug',
            field=models.SlugField(default='6ZMHeImxV9lUTyKYvEjd', max_length=250, unique=True, unique_for_date='publish'),
        ),
    ]
