from django.db import models

# Create your models here.


class Request(models.Model):
    title = models.CharField(verbose_name="Titre")
    QUESTION = 0
    NEW_TEAM = 1
    DATE = 2
    TYPE_CHOICE = (
        (QUESTION, "Question"),
        (NEW_TEAM, "Nouveau groupe"),
        (DATE, "Rendez-vous")
    )
    type = models.IntegerField(choices=TYPE_CHOICE, default=QUESTION)


    class Meta:
        verbose_name = "Demande"