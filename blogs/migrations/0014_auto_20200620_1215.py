# Generated by Django 3.0.7 on 2020-06-20 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0013_auto_20200620_1145'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='displayName',
            new_name='display_name',
        ),
        migrations.AddField(
            model_name='setting',
            name='google_adsense',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='setting',
            name='google_analytics',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='description',
            field=models.CharField(blank=True, max_length=300, verbose_name='Mô tả'),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.CharField(blank=True, max_length=300, verbose_name='Mô tả'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='ads',
            field=models.ManyToManyField(blank=True, to='blogs.Ad', verbose_name='Quảng cáo'),
        ),
    ]