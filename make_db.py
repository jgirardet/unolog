#populate new db
import sys
from random import choice as ch

from tests.factories import *

from ordonnances.models import Ordonnance
from patients.models import Patient
from unousers.models import UnoUser

# sys.path.append('./unolog')  # isort:skip



def populate():
    FacPatient.create_batch(20)
    FacUnoUser.create_batch(3)
    for i in range(60):
        FacObservation.create(
            owner=ch(UnoUser.objects.all()), patient=ch(Patient.objects.all()))
    for i in range(60):
        FacOrdonnance.create(
            owner=ch(UnoUser.objects.all()), patient=ch(Patient.objects.all()))
    for i in range(60):
        FacLigneMedicament.create(ordonnance=ch(Ordonnance.objects.all()))
    # FacOrdonnance.create_batch(30)
