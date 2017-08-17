from unologbase.models import Patient
from mixer.backend.django import mixer
import pytest
from django.db import IntegrityError
from string import capwords
import datetime
from django.core.exceptions import ValidationError

pytestmark = pytest.mark.django_db

class TestPatient:
	""" Class to Test Patient model
	"""
	
	def test_string(self):
		"""
		test autoput of str
		"""
		a = mixer.blend(Patient)
		assert a.__str__() == a.firstname+' '+a.name




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

	# def test_name_with_capworlods(self):
	# 	"""
	# 	ensure firstname in db is capword format
	# 	"""
	# 	a = mixer.blend(Patient)
	# 	a.firstname = "lihlih lih li jhlijh"
	# 	b = Patient.objects.create(a.name, a.firstname, a.birthdate)
	# 	c = Patient.objects.get(id=b.id)
	# 	assert c.firstname == capwords(a.firstname), "should pass iif moedl set"

	# def test_birhtdate_not_in_future(self):
	# 	"""
	# 	not bonr in future
	# 	"""
	# 	a = mixer.blend(Patient)
	# 	a.birthdate = datetime.date(2200, 1,1)
	# 	with pytest.raises(ValidationError):
	# 		b = Patient.objects.create(a.name, a.firstname, a.birthdate)
		
