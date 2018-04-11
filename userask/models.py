from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

# Create your models here.


class UserAsk(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Utilisateur")
    image = models.ImageField(verbose_name="Image", blank=True, null=True)

    class Meta:
        verbose_name = "Utilisateur Ask"