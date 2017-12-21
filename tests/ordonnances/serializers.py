from ordonnances.serializers import OrdonnanceSerializer


class TestOrdonnanceSerializer:
    def test_route_detail_url(self):
        a = OrdonnanceSerializer()
        assert a.fields['url'].view_name == "ordonnance-detail"
