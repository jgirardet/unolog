import os
import random

import factory
import pytest
from actes.models import Observation
from django.contrib.auth import get_user_model
from patients.models import Patient
from tests.patients.factory import FacPatient

# from pytest_django.fixtures import db

User = get_user_model()

# assert 1 == sys.path
"""
PAtients
"""

@pytest.fixture(scope='function', autouse=True)
def fpatient(db):
    """
    DRF apiclient
    """
    return  FacPatient

"""
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

    return factory.build(dict, FACTORY_CLASS=FacPatient)


@pytest.fixture(autouse=True)
def patient(patient_dict):
    p = Patient.objects.create(**patient_dict)
    return p


@pytest.fixture(autouse=True, scope='function')
def patientd(db):
    return mixer.blend(Patient)


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
def observation(patient, testuser, db):
    """
    fixture for observation instance
    """
    o = mixer.blend(Observation, patient=patient, owner=testuser)
    return o
