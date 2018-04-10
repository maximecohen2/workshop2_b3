# Generated by Django 2.0.4 on 2018-04-10 12:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='max_user',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name="nombre d'étudiant max"),
        ),
    ]