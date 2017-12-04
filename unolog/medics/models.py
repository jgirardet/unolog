from django.db import models

from actes.models import Ordonnance

# Create your models here.


class Medic(models.Model):
    """
    Base model for medics
    """
    cip = models.CharField(max_length=20)
    nom = models.CharField(max_length=200)
    posologie = models.CharField(max_length=200)
    duree = models.PositiveIntegerField()  # en jours
    ald = models.BooleanField(default=False)
    ordonnance = models.ForeignKey(
        Ordonnance, on_delete=models.CASCADE, related_name="medics")

    def __str__(self):
        return self.nom
