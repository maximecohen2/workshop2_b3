# Generated by Django 2.0.4 on 2018-04-12 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0009_team_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='image'),
        ),
    ]
