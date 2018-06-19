# Generated by Django 2.0.5 on 2018-06-19 02:04

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cedoc', '0005_auto_20180618_1731'),
    ]

    operations = [
        migrations.CreateModel(
            name='AudioVisual',
            fields=[
                ('doc_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cedoc.Doc')),
                ('dateProduction', models.DateField(default=django.utils.timezone.now, verbose_name='Production Field')),
                ('country', models.CharField(default='Brasil', max_length=50, verbose_name='Country of Production')),
                ('state', models.CharField(default='DF', max_length=50, verbose_name='Country of Production')),
                ('city', models.CharField(default='Brasília', max_length=50, verbose_name='Country of Production')),
                ('locationProduction', models.CharField(default='<django.db.models.fields.CharField>,<django.db.models.fields.CharField>,<django.db.models.fields.CharField>', max_length=200, verbose_name='Location of Production')),
                ('duration', models.DurationField(default=datetime.timedelta(0), verbose_name='Video Duration')),
                ('File', models.FileField(blank=True, upload_to='video/')),
            ],
            bases=('cedoc.doc',),
        ),
        migrations.RemoveField(
            model_name='audiofile',
            name='doc_ptr',
        ),
        migrations.RemoveField(
            model_name='videofile',
            name='doc_ptr',
        ),
        migrations.DeleteModel(
            name='AudioFile',
        ),
        migrations.DeleteModel(
            name='VideoFile',
        ),
    ]