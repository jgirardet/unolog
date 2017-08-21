import random

import pytest

from unologbase.models import Patient


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
    from mixer.backend.django import Mixer, mixer
    m = Mixer(commit=False)
    p = m.blend(
        Patient,
        street=mixer.FAKE,
        city=mixer.FAKE,
        postalcode=str(random.randrange(1, 99999)),
        phonenumber='0' + str(random.randrange(100000000, 899999999)), )
    return p
