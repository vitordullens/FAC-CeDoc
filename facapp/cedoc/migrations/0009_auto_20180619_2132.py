# Generated by Django 2.0.5 on 2018-06-20 00:32

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cedoc', '0008_auto_20180619_2031'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate', models.CharField(help_text='Name of Certificate', max_length=100, verbose_name='Certificate')),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now, verbose_name='Certificate Date')),
            ],
        ),
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('materia', models.CharField(help_text='Nome da Matéria', max_length=100, verbose_name='Materia')),
                ('author', models.CharField(help_text='Nome da Matéria', max_length=100, verbose_name='Author')),
            ],
        ),
        migrations.AddField(
            model_name='audiovisual',
            name='material',
            field=models.CharField(blank=True, max_length=100, verbose_name='Original Material'),
        ),
        migrations.AddField(
            model_name='index',
            name='paper',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cedoc.AudioVisual'),
        ),
        migrations.AddField(
            model_name='certificate',
            name='paper',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cedoc.AudioVisual'),
        ),
    ]
