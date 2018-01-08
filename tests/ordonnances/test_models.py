import random

import factory
import pytest
from ordonnances.models import Conseil, LigneOrdonnance, Medicament, Ordonnance
from tests.factories import *

pytestmark = pytest.mark.django_db


class TestOrdonnance:
    def test_get_lignes(self):
        "every type is fetched"
        o = FacOrdonnance()
        l = random.choices((FacMedicament, FacConseil), k=10)
        e = [i(ordonnance=o) for i in l]
        assert set(e) == set(o.get_lignes())

    def test_get_lignes_position(self):
        o = FacOrdonnance()
        l = random.choices((FacMedicament, FacConseil), k=5)
        e = [i(ordonnance=o) for i in l]
        random.shuffle(e)
        o.ordre = ''
        for i in e:
            i._update_ordre()

        assert set(e) == set(o.get_lignes())

    # def test_update_ordre(self):
    #     o = FacOrdonnance()
    #     l = random.choices((FacMedicament, FacConseil), k=5)
    #     e = [i(ordonnance=o) for i in l]
    #     instance = e[1]
    #     o.update_ordre(instance, 4)
    #     assert


class TestLigneManager:
    def test_update_ordre(self):
        a = FacMedicament()
        b = FacMedicament(ordonnance=a.ordonnance)
        assert a.ordonnance.ordre == 'Medicament-{};Medicament-{}'.format(
            a.id, b.id)

    def test_newline_non_extra_kwargs(self):
        a = factory.build(
            dict, FACTORY_CLASS=FacMedicament, ordonnance=FacOrdonnance())
        a["rin"] = "rien"
        with pytest.raises(AssertionError):
            Medicament.objects.new_ligne(**a)


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

    def test_delete(self):
        a = FacMedicament()
        b = FacMedicament(ordonnance=a.ordonnance)
        a.delete()
        assert b.ordonnance.ordre == b.nom_id
