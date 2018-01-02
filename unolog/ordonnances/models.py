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
    position = models.CharField(max_length=300)

    def __str__(self):
        return str(self.id)


class LigneOrdonnance(models.Model):
    """
    Base Class for each item on Ordonnance
    """

    ordonnance = models.ForeignKey(
        Ordonnance, related_name="%(class)ss", on_delete=models.CASCADE)
    ald = models.BooleanField(default=False)

    class Meta:
        abstract = True

    @property
    def nom_id(self):
        return self.__class__.__name__.lower() + str(self.id)


class Medicament(LigneOrdonnance):
    """
    Medicament model
    """
    cip = models.CharField(max_length=30)
    nom = models.CharField(max_length=200)
    posologie = models.CharField(max_length=200)
    duree = models.PositiveIntegerField()  # en jours

    def __str__(self):
        return self.nom


class Conseil(LigneOrdonnance):
    """
    Base model pour des conseils
    """
    texte = models.TextField()

    def __str__(self):
        return self.contenu
