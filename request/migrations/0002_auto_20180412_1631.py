# Generated by Django 2.0.4 on 2018-04-12 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='request',
            old_name='Statut',
            new_name='statut',
        ),
        migrations.AddField(
            model_name='request',
            name='cout',
            field=models.PositiveIntegerField(default=44, verbose_name='cout en token'),
            preserve_default=False,
        ),
    ]