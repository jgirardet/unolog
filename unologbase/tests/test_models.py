import datetime
from string import capwords

import pytest
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from mixer.backend.django import Mixer, mixer
from unologbase.models import Patient

pytestmark = pytest.mark.django_db


# @pytest.mark.usefixtures('patient_nodb')
class TestPatient:
    """
    Class to Test Patient model
    """

    def test_string(self):
        """
        test autoput of str
        """
        a = mixer.blend(Patient)
        assert a.__str__() == a.firstname + ' ' + a.name

    def test_fields_with_capwords(self, patient_nodb):
        """
        must be caps words :
            name
            firstname
            city
        """
        a = patient_nodb
        a.name = a.name.lower()
        a.firstname = a.firstname.lower()
        a.city = a.city.lower()
        a.save()

        assert a.name == capwords(a.name)
        assert a.firstname == capwords(a.firstname)
        assert a.city == capwords(a.city)

    def test_blank_true_for_non_required_fields(self):
        """
        mixer don't autopopulate blank fields
        """
        a = Mixer(commit=False).blend(Patient)
        a.save()
        b = Patient.objects.get(id=a.id)

        assert a == b


class TestBaseActe:
    """
    Class for testing abstracted BaseACte
    """


class TestObservation:
    """
    model Observation tesing
    """

    def test_motif_cant_be_blank(self, observation_nodb):
        o = observation_nodb
        o.motif = ""
        o.save()
