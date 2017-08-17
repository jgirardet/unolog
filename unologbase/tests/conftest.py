import pytest
from unologbase.models import Patient

@pytest.fixture(scope='module', autouse=True)
def apiclient():
	"""
	DRF apiclient
	"""
	from rest_framework.test import APIClient
	return APIClient()


@pytest.fixture(autouse=True)
def patient_nodb():
	"""
	give none persistent data of patient model
	"""
	from mixer.backend.django import Mixer
	m = Mixer(commit=False)
	p = m.blend(Patient)
	[p.__dict__.pop(k) for k in ('id','_state')]
	return p

