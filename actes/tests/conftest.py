import random

import pytest
from mixer.backend.django import Mixer, mixer
from pytest_django.fixtures import db

from actes.models import Observation
from patients.models import Patient
from patients.tests.conftest import patient_dict
from unousers.tests.conftest import testuser


@pytest.fixture(autouse=True, scope='function')
def observation_f(patient_dict, testuser, db):
    """
    fixture for observation instance
    """
    p = Patient.objects.create(**patient_dict)
    o = mixer.blend(Observation, patient=p, owner=testuser)
    return o
