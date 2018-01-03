from actes.models import BaseActe
from django.db import models


class Ordonnance(BaseActe):
    """
    ORdonnance pour  les médicaments.

    medic : un médicament
    duree : durée de l'ordonnance.
    oar : X time
    """

    # medics = models.ManyToManyField(Medic, related_name="medics")
    ordre = models.CharField(max_length=300, blank=True)

    def get_lines(self):
        #pour avoir chaque type différent de ligne
        m = self.medicaments.all()
        n = self.conseils.all()
        lignes = m + n

    def __str__(self):
        return str(self.id)


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

    @property
    def nom_id(self):
        return self.__class__.__name__+"-" + str(self.id)

    def save(self, *args, **kwargs):
        if not self.id: #new thing alwayas dded first
            super().save(*args, **kwargs)
            ordo = Ordonnance.objects.get(id=self.ordonnance.id)
            ordo.ordre = ordo.ordre + ";" + self.nom_id
            ordo.save()

        else:
            #now about update
            ordre = self.ordonnance.ordre.split(";")
            try:
                ordre.remove(self.nom_id)
            except:
                pass
            ordre.insert(self.position, self.nom_id)
            self.ordonnance.ordre = ";".join(ordre)
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

    # def __str__(self):
    #     return self.texte
