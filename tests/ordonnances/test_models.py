import random

from tests.factories import *

import factory
import pytest
from ordonnances.models import Conseil, LigneOrdonnance, Medicament, Ordonnance

pytestmark = pytest.mark.django_db

# class TestOrdonnance:
#     def test_get_lignes(self, ordonnance):
#         o = FacOrdonnance()
#         l = random.choices((FacMedicament, FacConseil), k=10)
#         e = [i(ordonnance=o) for i in l]
#         assert set(e) == set(o.get_lignes())


class TestLigneManager:
    def test_newline_non_extra_kwargs(self):
        a = factory.build(
            dict, FACTORY_CLASS=FacMedicament, ordonnance=FacOrdonnance())
        a["rin"] = "rien"
        with pytest.raises(AssertionError):
            Medicament.objects.new_ligne(**a)

    def test_newline_saves_position(self):
        o = FacOrdonnance()
        [FacMedicament(ordonnance=o) for i in range(5)]
        a = FacMedicament(ordonnance=o)
        assert a.position == 5


class TestLigneOrdonnance:
    def test_nom_id(self):
        a = FacMedicament()
        e = a.id
        assert a.nom_id == "Medicament-" + str(e)

    def test_save(self):
        a = FacMedicament()
        o = a.ordonnance
        import time
        time.sleep(0.01)
        b = FacMedicament(ordonnance=o)
        assert o.created < o.modified
