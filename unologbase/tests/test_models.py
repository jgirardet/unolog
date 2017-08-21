import datetime
from string import capwords

import pytest
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from mixer.backend.django import mixer

from unologbase.models import Patient

pytestmark = pytest.mark.django_db


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

    def test_name_and_firstname_with_capwords(self):
        """
ensure name and firstnamein db is capword format
"""
        a = mixer.blend(Patient, commit=False)
        a.name = a.name.lower()
        a.firstname = a.firstname.lower()
        a.save()

        assert a.name == capwords(a.name)
        assert a.firstname == capwords(a.firstname)

#     def test_model_ok_with_only_requiered_field(self):
#         a = Patient(
#             name="momok mok mo",
#             firstname='mokmokmokmo',
#             birthdate=datetime.date.today())
#         b = a.save()


    # def test_birhtdate_not_in_future(self):
    # 	"""
    # 	not bonr in future
    # 	"""
    # 	a = mixer.blend(Patient)
    # 	a.birthdate = datetime.date(2200, 1,1)
    # 	with pytest.raises(ValidationError):
    # 		b = Patient.objects.create(a.name, a.firstname, a.birthdate)
