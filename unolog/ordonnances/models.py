from django.db import models
from django.utils import timezone

from actes.models import BaseActe


class Ordonnance(BaseActe):
    """
    ORdonnance pour  les médicaments.

    medic : un médicament
    duree : durée de l'ordonnance.
    oar : X time
    """

    # medics = models.ManyToManyField(Medic, related_name="medics")
    ordre = models.CharField(max_length=300, blank=True)

    def get_lignes(self):
        #pour avoir chaque type différent de ligne
        pass

    def __str__(self):
        return str(self.id)


class LigneManager(models.Manager):
    def new_ligne(self, **kwargs):
        #check allowed kwargs
        fields = set([i.name for i in self.model._meta.get_fields()])
        assert not set(kwargs) - fields, "kwargs should be in model fields"

        ligne = self.model(**kwargs)
        ligne.save()
        print(ligne.ordonnance_id)
        ligne.ordonnance.ordre = ";".join((ligne.ordonnance.ordre,
                                           ligne.nom_id))
        ligne.save()
        return ligne

    def update_ligne(self, **kwargs):
        pass
        #
        # else:
        #     #now about update
        #     ordre = self.ordonnance.ordre.split(";")
        #     try:
        #         ordre.remove(self.nom_id)
        #     except:
        #         pass
        #     ordre.insert(self.position, self.nom_id)
        #     self.ordonnance.ordre = ";".join(ordre)
        #     super().save(*args, **kwargs)


class LigneOrdonnance(models.Model):
    """
    Base Class for each item on Ordonnance
    """

    ordonnance = models.ForeignKey(
        Ordonnance, related_name="%(class)ss", on_delete=models.CASCADE)
    ald = models.BooleanField(default=False)
    position = models.IntegerField()

    class Meta:
        abstract = True

    objects = LigneManager()

    @property
    def nom_id(self):
        return self.__class__.__name__ + "-" + str(self.id)

    def save(self, *args, **kwargs):
        self.ordonnance.save()
        super().save()


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
        return self.texte[:20]
