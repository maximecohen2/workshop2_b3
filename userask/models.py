from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserAsk(models.Model):

    user = models.OneToOneField(User, on_delete=models.PROTECT, verbose_name="Utilisateur")
    image = models.ImageField(verbose_name="Image")

    class Meta:
        verbose_name = "Utilisateur Ask"