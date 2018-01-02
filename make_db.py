#populate new db
import sys
from random import choice as ch

from tests.factories import *

from ordonnances.models import Ordonnance
from patients.models import Patient
from unousers.models import UnoUser

# sys.path.append('./unolog')  # isort:skip


def populate():
    FacPatient.create_batch(3)
    FacUnoUser.create_batch(2)
    for i in range(20):
        FacObservation.create(
            owner=ch(UnoUser.objects.all()), patient=ch(Patient.objects.all()))
    for i in range(20):
        FacOrdonnance.create(
            owner=ch(UnoUser.objects.all()), patient=ch(Patient.objects.all()))
    for i in range(80):
        FacLigneMedicament.create(ordonnance=ch(Ordonnance.objects.all()))
    # FacOrdonnance.create_batch(30)


def reset_db():
    [i.delete() for i in Patient.objects.all()]
    [i.delete() for i in UnoUser.objects.all()[1:]]
