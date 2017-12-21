from django.conf import settings
from django.db import models

from patients.models import Patient


class BaseActe(models.Model):
    """
    Base Abstract class for for differnets actions
    made by usej
    """
    patient = models.ForeignKey(
        Patient, related_name="%(class)ss", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="%(class)ss",
        on_delete=models.PROTECT)

    class Meta:
        abstract = True


class Observation(BaseActe):
    """
    A small text of  user about a patient

    motif : purpose of the visit. can't be blank.this is the most minimam
    thing a user schould enter.
    """
    motif = models.CharField(max_length=40, blank=False)
    body = models.TextField(blank=True)

    def __str__(self):
        return self.motif


class Ordonnance(BaseActe):
    """
    ORdonnance pour  les médicaments.

    medic : un médicament
    duree : durée de l'ordonnance.
    oar : X time
    """

    # medics = models.ManyToManyField(Medic, related_name="medics")

    def __str__(self):
        return self.owner.username + ' ' + self.created.strftime(
            "%a, %d %b %Y %H")


"""
BAseActe:
non modifiable if not today
Observation :
    TA/pouls
    conclusion

ordonnance
vaccin
certif
    titre
    texte
courries
    dest
    corps
courriers reçus
    spé
    nom
    contenu
    pdf
examens:
    type
    effecteur
    pdf
REGROUPER courrier et examens ?

bio
antécédants
intolérances
allergies
"""
