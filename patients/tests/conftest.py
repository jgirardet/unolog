import random

import pytest
from mixer.backend.django import Mixer, mixer

from actes.models import Observation
from patients.models import Patient


@pytest.fixture(scope='session', autouse=True)
def apiclient():
    """
    DRF apiclient
    """
    from rest_framework.test import APIClient
    return APIClient()


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
        email=mixer.FAKE, )

    p.__dict__.pop('_state')
    p.__dict__.pop('id')
    return p.__dict__
