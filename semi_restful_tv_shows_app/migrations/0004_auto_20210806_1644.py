# Generated by Django 2.2 on 2021-08-06 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semi_restful_tv_shows_app', '0003_auto_20210805_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shows',
            name='release_date',
            field=models.DateTimeField(),
        ),
    ]
