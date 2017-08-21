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

    # def test_birhtdate_not_in_future(self):
    # 	"""
    # 	not bonr in future
    # 	"""
    # 	a = mixer.blend(Patient)
    # 	a.birthdate = datetime.date(2200, 1,1)
    # 	with pytest.raises(ValidationError):
    # 		b = Patient.objects.create(a.name, a.firstname, a.birthdate)
