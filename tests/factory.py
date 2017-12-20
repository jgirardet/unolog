import sys

import factory
from faker import Faker
from patients.models import Patient

sys.path.append('../unolog')

fk = factory.Faker

class FacPatient(factory.django.DjangoModelFactory):
    class Meta:
        model = Patient


    name = fk('last_name')
    firstname = factory.Faker('first_name')
