# Generated by Django 2.0.4 on 2018-04-12 15:44

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='nom')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('file', models.FileField(blank=True, null=True, upload_to='', verbose_name='fichier')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='image')),
                ('date_start', models.DateField(verbose_name='date de depart du projet')),
                ('date_end', models.DateField(verbose_name='date de fin du projet')),
                ('token', models.IntegerField(verbose_name='nombre de jetons par groupes')),
            ],
            options={
                'verbose_name': 'Projet',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='nom')),
                ('max_user', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name="nombre d'étudiant max")),
                ('private', models.BooleanField(default=True, verbose_name='privé')),
                ('token_remain', models.PositiveIntegerField(verbose_name='token restant')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='project.Project', verbose_name='projet')),
            ],
            options={
                'verbose_name': 'Groupe',
            },
        ),
    ]
