from django.contrib.auth import get_user_model
from tests.factories import *

import factory
import pytest

# from pytest_django.fixtures import db

User = get_user_model()

# assert 1 == sys.path
"""
PAtients
"""


@pytest.fixture(autouse=True, scope='function')
def patientd():
    """
    just a dict, not saved
    """

    return factory.build(dict, FACTORY_CLASS=FacPatient)


@pytest.fixture(autouse=True)
def patient(db):
    """
    saved to database
    """
    return FacPatient()


@pytest.fixture(scope='function', autouse=True)
def apiclient(db):
    """
    DRF apiclient
    """
    u = FacUnoUser()
    from rest_framework.test import APIClient
    client = APIClient()
    client.force_authenticate(user=u)
    return client


"""
USers
"""


#
@pytest.fixture(autouse=True, scope='function')
def testuser(db):

    return FacUnoUser()


# """
# actes
# """


@pytest.fixture(autouse=True, scope='function')
def observation(db):
    """
    fixture for observation instance
    """
    return FacObservation()


#"""
#Ordonnances
#""""
@pytest.fixture(autouse=True)
def ordonnance(db):
    return FacOrdonnance()
