from django.contrib.contenttypes.fields import (GenericForeignKey,
                                                GenericRelation)
from django.contrib.contenttypes.models import ContentType
from django.db import models

from actes.models import BaseActe


class Ordonnance(BaseActe):
    """
    ORdonnance pour  les médicaments.

    medic : un médicament
    duree : durée de l'ordonnance.
    oar : X time
    """

    # medics = models.ManyToManyField(Medic, related_name="medics")

    def __str__(self):
        return str(self.id)


class LigneOrdonnance(models.Model):
    """
    Base Class for each item on Ordonnance
    """
    position = models.PositiveIntegerField()
    ordonnance = models.ForeignKey(
        Ordonnance, on_delete=models.CASCADE, related_name="lignes")
    ald = models.BooleanField(default=False)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    contenu = GenericForeignKey()

    def __str__(self):
        return 'ordo : ' + self.ordonnance.__str__() + ' position : ' + str(
            self.position) + ' : ' + self.contenu.__str__()


class Medicament(models.Model):
    """
    Medicament model
    """
    cip = models.CharField(max_length=30)
    nom = models.CharField(max_length=200)
    posologie = models.CharField(max_length=200)
    duree = models.PositiveIntegerField()  # en jours
    ligne = GenericRelation(LigneOrdonnance, related_query_name='medicament')

    def __str__(self):
        return self.nom


class Conseil(models.Model):
    """
    Base model pour des conseils
    """
    texte = models.TextField()
    ligne = GenericRelation(LigneOrdonnance, related_query_name='conseil')

    def __str__(self):
        return self.contenu
