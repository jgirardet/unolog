import pytest
from actes.serializers import ObservationSerializer


class TestObservationSerializer:
    def test_route_detail_url(self):
        a = ObservationSerializer()
        assert a.fields['url'].view_name == "observation-detail"
