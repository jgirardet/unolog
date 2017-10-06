import pytest
from django.contrib.auth import get_user_model
from mixer.backend.django import Mixer, mixer
from pytest_django.fixtures import db

# pytestmark = pytest.mark.django_db


@pytest.fixture(autouse=True, scope='function')
def testuser(db):
    model = get_user_model()
    u = mixer.blend(model)
    return u
