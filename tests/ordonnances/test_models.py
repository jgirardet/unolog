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

    def test_get_querysets(self):
        o = FacOrdonnance()
        #le test est valadble que pour ce cas
        o.TYPE_ACTIFS == (
            "Medicament",
            "Conseil",
        )
        FacConseil.create_batch(ordonnance=o, size=3)
        FacMedicament.create_batch(ordonnance=o, size=3)
        qss = {}
        qss['Medicament'] = o.medicaments.all()
        qss['Conseil'] = o.conseils.all()
        e = o._get_querysets()

        assert set(qss['Medicament']) == set(e['Medicament'])
        assert set(qss['Conseil']) == set(e['Conseil'])
        assert len(o.TYPE_ACTIFS) == len(e), "len should be the same"

    def test_get_new_ordre(self):
        o = FacOrdonnance()
        l = random.choices((FacMedicament, FacConseil), k=6)
        qs = o._get_querysets()
        o.ordre = ''
        m = list(o.medicaments.all())
        m.extend(list(o.conseils.all()))
        assert set(m) == set(o._get_new_ordre(qs))
        assert ';'.join([i.nom_id for i in m]) == o.ordre


class TestLigneManager:
    def test_newline_non_extra_kwargs(self):
        a = factory.build(
            dict, FACTORY_CLASS=FacMedicament, ordonnance=FacOrdonnance())
        a["rin"] = "rien"
        with pytest.raises(AssertionError):
            Medicament.objects.new_ligne(**a)

    def test_new_ligne(self):
        o = FacOrdonnance()
        m = factory.build(dict, FACTORY_CLASS=FacMedicament, ordonnance=o)
        obj = Medicament.objects.create(**m)
        assert isinstance(obj, Medicament)
        assert obj.id


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
        assert o.created < o.modified, "modified non modifié, ordonnance pas sauvée"

    def test_delete(self):
        a = FacMedicament()
        b = FacMedicament(ordonnance=a.ordonnance)
        a.delete()
        assert b.ordonnance.ordre == b.nom_id

    def test_update_ordre(self):
        a = FacMedicament()
        b = FacMedicament(ordonnance=a.ordonnance)
        assert a.ordonnance.ordre == 'Medicament-{};Medicament-{}'.format(
            a.id, b.id)


class TestMedicament:
    def test_str(self):
        a = FacMedicament()
        assert a.nom == a.__str__()


class TestConseil:
    def test_str(self):
        a = FacConseil()
        assert a.__str__() == a.texte[:20]
