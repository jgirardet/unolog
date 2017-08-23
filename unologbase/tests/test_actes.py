from mixer.backend.django import Mixer, mixer

import pytest
from unologbase.models import Patient

pytestmark = pytest.mark.django_db

class TestObservation:
    """
    model Observation tesing
    """

    def test_str(self, observation_nodb):
        o = observation_nodb
        o.save()
        assert o.__str__() == o.motif
