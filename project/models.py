from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.


class Project(models.Model):

    name = models.CharField(max_length=100, verbose_name="nom")
    description = models.TextField(blank=True, verbose_name="description")
    file = models.FileField(verbose_name="fichier", null=True, blank=True)
    date_start = models.DateField(verbose_name='date de depart du projet')
    date_end = models.DateField(verbose_name='date de fin du projet')
    token = models.IntegerField(verbose_name='nombre de jetons par groupes')

    class Meta:
        verbose_name = "Projet"


class Team(models.Model):

    name = models.CharField(max_length=100, verbose_name="nom")
    project = models.ForeignKey('Project', on_delete=models.PROTECT, verbose_name="projet")
    max_user = models.PositiveIntegerField(verbose_name="nombre d'étudiant max", validators=[MinValueValidator(1)])
    private = models.BooleanField(verbose_name="privé", default=True)
    token_remain = models.PositiveIntegerField("token restant")
    users = models.ManyToManyField(User, verbose_name='membres du groupe')

    class Meta:
        verbose_name = "Groupe"
