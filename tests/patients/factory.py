import datetime
import sys

from django.utils import timezone

import factory
from faker import Faker
from patients.models import Patient

sys.path.append('../unolog')

fk = factory.Faker
tz = timezone.tzinfo


class FacPatient(factory.django.DjangoModelFactory):
    class Meta:
        model = Patient

    name = fk('last_name', locale="fr_FR")
    firstname = fk('first_name', locale="fr_FR")
    birthdate = fk('past_date', start_date="-30y", tzinfo=datetime.tzinfo())
    street = fk('street_address', locale="fr_FR")
    city = fk('city', locale="fr_FR")
    postalcode = fk('zipcode')
    phonenumber = "0381395685"
    email = fk('email', locale="fr_FR")
    alive = True
    sexe = fk('pybool')
