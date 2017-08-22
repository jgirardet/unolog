import random

import pytest

from mixer.backend.django import Mixer, mixer
from unologbase.models import (
        Patient,
        Observation,
        )


@pytest.fixture(scope='session', autouse=True)
def apiclient():
    """
    DRF apiclient
    """
    from rest_framework.test import APIClient
    return APIClient()


@pytest.fixture(autouse=True, scope='function')
def patient_nodb():
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
        phonenumber='0' + str(random.randrange(100000000, 899999999)), )
    return p

@pytest.fixture(autouse=True, scope='function')
def observation_nodb(patient_nodb):
    """
    fixture for observation instance
    """
    p = patient_nodb
    p.save()
    o = Mixer(commit=False).blend(
            Observation,
            patient = p,
            )
    return o
