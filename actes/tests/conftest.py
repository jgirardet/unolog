import random

import pytest
from mixer.backend.django import Mixer, mixer

from actes.models import Observation
from patients.models import Patient


@pytest.fixture(autouse=True, scope='function')
def observation_nodb(patient_dict):
    """
    fixture for observation instance
    """
    p = Patient.objects.create(**patient_dict)
    o = Mixer(commit=False).blend(
        Observation,
        patient=p, )
    return o
