# Generated by Django 2.0.4 on 2018-04-11 15:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20180410_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='date_end',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='date de fin du projet'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='date_start',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='date de depart du projet'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='token',
            field=models.IntegerField(default=1, verbose_name='nombre de jetons actuel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='token_used',
            field=models.IntegerField(default=1, verbose_name='nombre de jetons utilisé'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='fichier'),
        ),
    ]