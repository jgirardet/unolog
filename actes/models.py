from django.conf import settings
from django.db import models

from patients.models import Patient


class BaseActeManager(models.Manager):
    """
    custom managers for all base act
    """

    def create(self, **kwargs):
        # recall base create
        return super(BaseActeManager, self).create(**kwargs)


class BaseActe(models.Model):
    """
    Base Abstract class for for differnets actions
    made by usej
    """
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

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
