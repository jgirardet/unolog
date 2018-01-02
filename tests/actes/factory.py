import datetime
import random

from tests.patients.factory import FacPatient
from tests.unousers.factory import FacUnoUser

import factory

fk = factory.Faker


class FacBaseActe(factory.django.DjangoModelFactory):
    class Meta:
        abstract = True

    patient = factory.SubFactory(FacPatient)
    # created = fk('past_datetime', start_date='-30y')
    # modified= factory.LazyAttribute(lambda o: o.created + datetime.timedelta(days=1))
    owner = factory.SubFactory(FacUnoUser)


class FacObservation(FacBaseActe):
    class Meta:
        model = 'actes.Observation'

    motif = fk('sentence', nb_words=random.randint(1, 4))
    body = fk('paragraph', nb_sentences=random.randint(1, 10))
