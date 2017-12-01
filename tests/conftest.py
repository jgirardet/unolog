import os
import random

import pytest
from actes.models import Observation
from django.contrib.auth import get_user_model
from mixer.backend.django import Mixer, mixer
from patients.models import Patient

# from pytest_django.fixtures import db

User = get_user_model()

# assert 1 == sys.path
"""
PAtients
"""


@pytest.fixture(scope='function', autouse=True)
def apiclient(db):
    """
    DRF apiclient
    """
    model = get_user_model()
    u = mixer.blend(model)
    from rest_framework.test import APIClient
    client = APIClient()
    client.force_authenticate(user=u)
    return client


@pytest.fixture(autouse=True, scope='function')
def patient_dict():
    """
    give none persistent data of patient model

    mixer doesn't populate blank fields by dfault
    """
    m = Mixer(commit=False)
    p = m.blend(
        Patient,
        street=mixer.FAKE,
        city=mixer.FAKE,
        postalcode=str(random.randrange(1, 99999)),
        phonenumber='0' + str(random.randrange(100000000, 899999999)),
        email=mixer.FAKE,
    )

    p.__dict__.pop('_state')
    p.__dict__.pop('id')
    return p.__dict__.copy()


"""
USers
"""


@pytest.fixture(autouse=True, scope='function')
def testuser(db):

    return mixer.blend(get_user_model())


"""
actes
"""


@pytest.fixture(autouse=True, scope='function')
def observation_f(patient_dict, testuser, db):
    """
    fixture for observation instance
    """
    p = Patient.objects.create(**patient_dict)
    o = mixer.blend(Observation, patient=p, owner=testuser)
    return o
