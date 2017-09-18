from string import capwords

import pytest
from mixer.backend.django import Mixer

from unologbase.models import Patient

pytestmark = pytest.mark.django_db

# @pytest.mark.usefixtures('patient_dict')


class TestPatient:
    """
    Class to Test Patient model
    """

    attrs = ('name', 'firstname', 'city')

    def test_string(self, patient_dict):
        """
        test autoput of str
        """
        a = Patient.objects.create(**patient_dict)

        assert a.__str__() == a.firstname + ' ' + a.name

    def test_fields_with_capwords_at_create(self, patient_dict):
        """
        must be caps words :
            name
            firstname
            city
        """
        attrs = self.attrs
        d = patient_dict
        for i in attrs:
            d[i] = d[i].lower()
        b = Patient.objects.create(**d)
        for i in attrs:
            assert getattr(b, i) == capwords(d[i])

    def test_fileds_with_capwords_at_update(self, patient_dict):
        b = Patient.objects.create(**patient_dict)
        for i in self.attrs:
            b.__dict__[i] = getattr(b, i).lower()
        b.save()
        for i in self.attrs:
            assert getattr(b, i) == capwords(patient_dict[i])

    def test_instance_update_capwords(self, patient_dict):
        b = Patient.objects.create(**patient_dict)
        a = "mkokmokmokmok"
        b.name = a
        b.save()
        assert b.name == capwords(a)

    def test_blank_true_for_non_required_fields(self):
        """
        mixer don't autopopulate blank fields
        """
        a = Mixer(commit=False).blend(Patient)
        a.save()
        b = Patient.objects.get(id=a.id)

        assert a == b
