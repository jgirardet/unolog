from unologbase.models import Patient
from mixer.backend.django import mixer, Mixer
import pytest
from unologbase.serializers import PatientSerializer
from rest_framework.test import (APIClient, APIRequestFactory, force_authenticate)
from rest_framework.reverse import reverse
import datetime
from rest_framework import serializers
from string import capwords
import datetime
# from conftest import apiclient

pytestmark = pytest.mark.django_db



# pytest.mark.usefixtures('apiclient')
# pytest.mark.usefixtures('patient_nodb')

class TestPatientSerializer:
	"""
	Class fort PatientSerializer testing
	"""
	def test_check_birthdate(self):
		"""
		check no bithdate later
		"""
		d = datetime.date(3000, 1, 1)
		p = Mixer(commit=False).blend(Patient)
		p.birthdate = d
		[p.__dict__.pop(k) for k in ('id', '_state')]
		s = PatientSerializer(data=p.__dict__)
		with pytest.raises(serializers.ValidationError):
			s.is_valid(raise_exception=True), "sould return validation error"


	# def test_create_turns_to_capword_name_and_firstname(self, patient_nodb):
	# 	# p = Mixer(commit=False).blend(Patient)
	# 	p = patient_nodb
	# 	p.name = p.name.lower()
	# 	# p.firstname = p.firstname.lower()
	# 	# [p.__dict__.pop(k) for k in ('id', '_state')]
	# 	s = PatientSerializer(data=p.__dict__)
	# 	s.is_valid()
	# 	n = s.create(s.validated_data)
	# 	# assert n.__str__() == capwords(p.firstname+" "+p.name)
	# 	assert n.__str__() == capwords(p.firstname+" "+p.name)

	def test_fix(self,apiclient):
		r = apiclient.get('/api')
		assert r.status_code == 404
