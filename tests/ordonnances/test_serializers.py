from tests.factories import *

import factory
from ordonnances.models import Medicament
from ordonnances.serializers import MedicamentSerializer, OrdonnanceSerializer


class TestOrdonnanceSerializer:
    def test_route_detail_url(self):
        #??????
        a = OrdonnanceSerializer()
        assert a.fields['url'].view_name == "ordonnance-detail"


class TestLigneOrdonnanceSerializer:
    def test_create(self):
        a = factory.build(
            dict, FACTORY_CLASS=FacMedicament, ordonnance=FacOrdonnance())
        m = MedicamentSerializer().create(a)

        assert isinstance(m, Medicament), "e should be e MEdicament instance"
        assert m.nom == a['nom']

    def test_update(self):
        a = FacMedicament()
        lid = a.ordonnance.id
