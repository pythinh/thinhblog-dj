# Generated by Django 3.0.7 on 2020-06-22 18:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0021_auto_20200623_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 22, 18, 7, 9, 768337, tzinfo=utc), verbose_name='Cập nhật'),
        ),
    ]