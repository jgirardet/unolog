import pytest
from mixer.backend.django import Mixer

from actes.models import Observation

pytestmark = pytest.mark.django_db


class TestObservation:
    """
    Class to test observtion model
    """

    def test_string(self, observation_f):
        # test __str__
        assert observation_f.__str__() == observation_f.motif
