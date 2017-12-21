import sys

import factory
from faker import Faker
from patients.models import Patient

sys.path.append('../unolog')

fk = factory.Faker

class FacPatient(factory.django.DjangoModelFactory):
    class Meta:
        model = Patient


    name = fk('last_name', locale ="fr_FR")
    firstname = fk('first_name', locale ="fr_FR")
    birthdate = fk('past_date', start_date="-90y")
    street = fk('street_address', locale ="fr_FR")
    city = fk('city', locale ="fr_FR")
    postalcode = fk('postcode', locale ="fr_FR")
    phonenumber = fk('msisdn', locale ="fr_FR")
    email = fk('email', locale ="fr_FR")
    alive = True
