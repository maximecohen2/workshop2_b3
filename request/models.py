from django.db import models

from project.models import Team


class Request(models.Model):
    cout = models.PositiveIntegerField(verbose_name='cout en token')
    title = models.CharField(verbose_name="Titre", max_length=50)
    QUESTION = 0
    NEW_TEAM = 1
    MEETING = 2
    TYPE_CHOICE = (
        (QUESTION, "Question"),
        (NEW_TEAM, "Nouveau groupe"),
        (MEETING, "Rendez-vous")
    )
    type = models.IntegerField(choices=TYPE_CHOICE, default=QUESTION)
    date = models.DateField(verbose_name='Demand date')
    team = models.ForeignKey(Team, verbose_name='Demands by team', on_delete=models.CASCADE)
    intervenant = models.CharField(verbose_name='Intervenant', max_length=50)
    WAITING = 0
    ACCEPTED = 1
    REFUSED = 2
    TYPE_STATUT = (
        (WAITING, "En attente"),
        (ACCEPTED, "Accepté"),
        (REFUSED, "Refusé")
    )
    statut = models.IntegerField(choices=TYPE_STATUT, default=WAITING)

    class Meta:
        verbose_name = "Demande"