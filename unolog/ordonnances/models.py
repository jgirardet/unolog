from itertools import chain
from operator import attrgetter

from django.apps import apps
from django.db import models
from django.utils import timezone

from actes.models import BaseActe


class Ordonnance(BaseActe):
    """
    ORdonnance pour  les médicaments.

    medic : un médicament
    duree : durée de l'ordonnance.
    oar : X time

    Chaque subClass de ligne/ordonnance doit apparaitre dans type_actif
    """

    ordre = models.CharField(max_length=300, blank=True)
    """
    TYPE_ACTIFS doit être utilisé à chaque fois qu'un opération
    doit retourner un mix des différents modele d'une ordonnances
    """

    TYPE_ACTIFS = (
        "Medicament",
        "Conseil",
    )

    @property
    def _get_actifs(self):
        types = []
        for name in self.TYPE_ACTIFS:
            yield apps.get_model('ordonnances', name)

    def get_lignes(self):
        #pour avoir chaque type différent de ligne
        lignes = []
        for mod in self.TYPE_ACTIFS:
            m = getattr(self, mod.lower() + 's')
            lignes.append(m.all())
        return sorted(chain(*lignes), key=attrgetter('position'))

    @property
    def nb_lignes(self):
        #pour avoir chaque type différent de ligne

        m = self.medicaments.count()
        c = self.conseils.count()
        return m + c

    def __str__(self):
        return str(self.id)


class LigneManager(models.Manager):
    def new_ligne(self, **kwargs):
        #check allowed kwargs
        fields = set([i.name for i in self.model._meta.get_fields()])
        assert not set(kwargs) - fields, "kwargs should be in model fields"

        ligne = self.model(**kwargs)
        # nb = ligne.ordonnance.
        print(ligne.ordonnance.created)
        ligne.save()
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
