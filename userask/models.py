from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

# Create your models here.


class UserAsk(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Utilisateur")
    image = models.ImageField(verbose_name="Image", blank=True, null=True)
    STUDENT = 1
    TEACHER = 2
    PEDAGOGY = 3
    ROLE = (
        (STUDENT, "Etudiant"),
        (TEACHER, "Intervenant"),
        (PEDAGOGY, "Pédagogie")
    )
    role = models.IntegerField(verbose_name="role de l'utilisateur", choices=ROLE, default=STUDENT)

    class Meta:
        verbose_name = "Utilisateur Ask"
