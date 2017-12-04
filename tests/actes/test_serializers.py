import pytest
from actes.serializers import ObservationSerializer, OrdonnanceSerializer


class TestObservationSerializer:
    def test_route_detail_url(self):
        a = ObservationSerializer()
        assert a.fields['url'].view_name == "observation-detail"


class TestOrdonnanceSerializer:
    def test_route_detail_url(self):
        a = OrdonnanceSerializer()
        assert a.fields['url'].view_name == "ordonnance-detail"
