# Generated by Django 2.0.5 on 2018-06-19 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cedoc', '0007_auto_20180619_1237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doc',
            name='fileType',
        ),
        migrations.AlterField(
            model_name='doc',
            name='fileFormat',
            field=models.CharField(choices=[('AN', 'Arquivo Físico'), ('UR', 'URL'), ('DG', 'Arquivo Digital')], default='DG', help_text='Escolha apenas 1 opção', max_length=2, verbose_name='Media Format'),
        ),
    ]
