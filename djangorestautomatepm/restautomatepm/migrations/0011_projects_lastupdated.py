# Generated by Django 3.0.7 on 2020-06-23 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restautomatepm', '0010_auto_20200623_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='lastupdated',
            field=models.DateField(default='2020-06-06'),
        ),
    ]
