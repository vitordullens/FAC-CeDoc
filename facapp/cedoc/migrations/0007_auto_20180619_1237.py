# Generated by Django 2.0.5 on 2018-06-19 15:37

import cedoc.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cedoc', '0006_auto_20180618_2304'),
    ]

    operations = [
        migrations.AddField(
            model_name='doc',
            name='url',
            field=models.URLField(blank=True, verbose_name='URL para Documento'),
        ),
        migrations.AlterField(
            model_name='audiovisual',
            name='File',
            field=models.FileField(blank=True, upload_to='video/', validators=[cedoc.validators.validate_AudioVisual]),
        ),
        migrations.AlterField(
            model_name='campusreporter',
            name='File',
            field=models.FileField(blank=True, upload_to='texts/reporter/', validators=[cedoc.validators.validate_CampusReporter]),
        ),
    ]
