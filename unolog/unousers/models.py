from django.contrib.auth.models import AbstractUser
from django.db import models

STATUT = ['docteur', 'secrétaire', 'interne', 'remplaçant']


class UnoUser(AbstractUser):
    """
    Base User class for unolog
    define statu
    """
    MEDECIN = "medecin"
    SECRETAIRE = "secretaire"
    INTERNE = "interne"
    REMPLACANT = "remplacant"
    STATUT = (
        (MEDECIN, 'Médecin'),
        (SECRETAIRE, 'Secrétaire'),
        (INTERNE, "Interne"),
        (REMPLACANT, "Remplaçant"),
    )

    statut = models.CharField(max_length=20)


"""

https://github.com/codingforentrepreneurs/srvup-rest-framework/blob/master/src/accounts/models.py
"""
