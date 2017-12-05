import pytest
from actes.models import Observation
from mixer.backend.django import Mixer

pytestmark = pytest.mark.django_db


class TestObservation:
    """
    Class to test observtion model
    """

    def test_string(self, observation):
        # test __str__
        assert observation.__str__() == observation.motif
