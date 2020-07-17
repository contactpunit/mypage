# Generated by Django 3.0.7 on 2020-07-17 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0004_auto_20200716_0305'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='caption',
            field=models.TextField(default='test'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='story',
            name='slug',
            field=models.SlugField(default='OjZd6YYi2UJDJCca9k4N3oZXspuMKwJM5tbVXMTkV22B2aIrijbnM5a5eBJJuZrdq7z8m7sTVu18Hw2J271dsqRYU8', max_length=250, unique=True, unique_for_date='publish'),
        ),
    ]
