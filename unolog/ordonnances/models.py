from actes.models import BaseActe
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Ordonnance(BaseActe):
    """
    ORdonnance pour  les médicaments.

    medic : un médicament
    duree : durée de l'ordonnance.
    oar : X time
    """

    # medics = models.ManyToManyField(Medic, related_name="medics")

    def __str__(self):
        return self.patient.name + ' ' + self.created.strftime(
            "%a, %d %b %Y %H")


class LigneOrdonnance(models.Model):
    """
    Base Class for each item on Ordonnance
    """
    position = models.PositiveIntegerField(unique=True)
    ordonnance = models.ForeignKey(
        Ordonnance, on_delete=models.CASCADE, related_name="%(class)ss")
    ald = models.BooleanField(default=False)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class Medicament(LigneOrdonnance):
    """
    Medicament model
    """
    cip = models.CharField(max_length=20)
    nom = models.CharField(max_length=200)
    posologie = models.CharField(max_length=200)
    duree = models.PositiveIntegerField()  # en jours

    def __str__(self):
        return self.nom


class Conseil(LigneOrdonnance):
    """
    Base model pour des conseils
    """
    contenu = models.TextField()
