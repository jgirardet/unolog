import pytest
from actes.models import Observation

pytestmark = pytest.mark.django_db


class TestObservation:
    """
    Class to test observtion model
    """

    def test_string(self, observation):
        # test __str__
        assert observation.__str__() == observation.motif

    def test_save(self, observation):
        assert observation.created == observation.modified
        import time
        time.sleep(1 / 100)
        observation.save()
        assert observation.created < observation.modified
