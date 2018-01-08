from itertools import chain
from operator import attrgetter

from actes.models import BaseActe
from django.apps import apps
from django.db import models
from django.utils import timezone


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

    def _get_querysets(self):
        #return dict of querysets for different ligne type
        querysets = {}
        for mod in self.TYPE_ACTIFS:
            lower = mod.lower() + 's'
            m = getattr(self, lower)
            querysets[mod] = m.all()
        return querysets

    def _get_new_ordre(self, querysets):
        """
        fonction de repli si la requête échoue (mauvais.ordre, .ordre et
        instance non concordant)
        """
        nouvelle_list = tuple(chain.from_iterable(querysets.values()))
        self.ordre = ';'.join([i.nom_id for i in nouvelle_list])
        self.save()
        return nouvelle_list

    def get_lignes(self):
        """
        retourne un liste de ligne dans l'ordre  à partir des _get_querysets
        et selon ordre

        """
        querysets = self._get_querysets()
        ordre = self.ordre.split(';')
        """
        #si l'ordre ne correspond pas aux lignes en ddb, on renvoi
        sans ordre
        """
        if sum(map(len, querysets.values())) != len(ordre):
            print("len pas ok")
            return self._get_new_ordre(querysets)

        #on suit l'ordre de o
        ordered = []
        try:
            for i in ordre:
                u = i.split('-')
                ordered.append(querysets[u[0]].get(id=u[1]))
        except:
            print("erreur pour l'ordered")
            return self._get_new_ordre(querysets)
        return ordered

    @property
    def nb_lignes(self):
        #pour avoir chaque type différent de ligne

        m = self.medicaments.count()
        c = self.conseils.count()
        return m + c

    # def update_ordre(self, instance,  new_pos ):
    #     pass

    def __str__(self):
        return str(self.id)


class LigneManager(models.Manager):
    def new_ligne(self, **kwargs):
        #check allowed kwargs
        fields = set([i.name for i in self.model._meta.get_fields()])
        assert not set(kwargs) - fields, "kwargs should be in model fields"

        ligne = self.model(**kwargs)

        ligne.save()

        ligne._update_ordre()
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

    class Meta:
        abstract = True

    objects = LigneManager()

    def _update_ordre(self):
        ordo = self.ordonnance
        ordo.ordre = ";".join((ordo.ordre, self.nom_id))
        ordo.ordre = ordo.ordre.strip(';')
        ordo.save()

    @property
    def nom_id(self):
        return self.__class__.__name__ + "-" + str(self.id)

    def save(self, *args, **kwargs):
        self.ordonnance.save()
        super().save()

    def delete(self, *args, **kwargs):
        #update ordonnace.ordre
        ordo = self.ordonnance
        ids = ordo.ordre.split(';')
        ids.remove(self.nom_id)
        ordo.ordre = ';'.join(ids)
        ordo.save()

        super().save(*args, **kwargs)


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
