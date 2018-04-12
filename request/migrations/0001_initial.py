# Generated by Django 2.0.4 on 2018-04-12 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project', '0002_team_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Titre')),
                ('type', models.IntegerField(choices=[(0, 'Question'), (1, 'Nouveau groupe'), (2, 'Rendez-vous')], default=0)),
                ('date', models.DateField(verbose_name='Demand date')),
                ('intervenant', models.CharField(max_length=50, verbose_name='Intervenant')),
                ('Statut', models.IntegerField(choices=[(0, 'En attente'), (1, 'Accepté'), (2, 'Refusé')], default=0)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Team', verbose_name='Demands by team')),
            ],
            options={
                'verbose_name': 'Demande',
            },
        ),
    ]
