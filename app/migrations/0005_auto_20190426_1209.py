# Generated by Django 2.2 on 2019-04-26 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20190426_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='label',
            name='color',
            field=models.CharField(blank=True, max_length=6),
        ),
        migrations.AlterField(
            model_name='project',
            name='guidelines',
            field=models.TextField(blank=True),
        ),
    ]
