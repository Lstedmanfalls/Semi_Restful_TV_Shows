# Generated by Django 2.2 on 2021-08-05 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semi_restful_tv_shows_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shows',
            name='release_date',
            field=models.DateField(verbose_name='%m/%d/%Y'),
        ),
    ]
