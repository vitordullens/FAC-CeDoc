# Generated by Django 2.0.5 on 2018-06-20 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cedoc', '0010_auto_20180620_1618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='video',
        ),
        migrations.AddField(
            model_name='audiovisual',
            name='video',
            field=models.ManyToManyField(to='cedoc.Categoria'),
        ),
    ]
