# Generated by Django 3.0.7 on 2020-06-23 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restautomatepm', '0004_phases_projectid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='company',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
