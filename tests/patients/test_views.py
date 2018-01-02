from string import capwords

from tests.patients.factory import FacPatient

import factory
import pytest
from patients.models import Patient
from patients.serializers import PatientSerializer
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIRequestFactory

pytestmark = pytest.mark.django_db

# @pytest.mark.usefixtures("apiclient")
class TestPatientView:
    """"
Base classe fo testing patient views
"""

    def test_retrieve_patient_list(self, apiclient):

        factory.create_batch(Patient, 12, FACTORY_CLASS=FacPatient)
        resp = apiclient.get(reverse('patient-list'))
        patients = Patient.objects.all()
        req = APIRequestFactory().get(reverse('patient-list'))
        ser = PatientSerializer(patients, many=True, context={'request': req})
        assert resp.data == ser.data

    def test_response_create_patient(self, apiclient, patientd):

        for i in Patient.attrs:  #turn capsword what is not saved
            patientd[i] = capwords(patientd[i])

        resp = apiclient.post(
            reverse('patient-list'), data=patientd, format='json')
        # import ipdb; ipdb.set_trace()
        print(resp.data)
        p = Patient.objects.get(pk=resp.data['pk'])
        [p.__dict__.pop(k) for k in ('id', '_state')]
        assert p.__dict__ == patientd
        assert resp.status_code == status.HTTP_201_CREATED

    def test_caps_test(self, apiclient, patientd):
        patientd['name'] = "Rebecca Ramirez DDS"
        for i in Patient.attrs:
            patientd[i] = capwords(patientd[i])

        resp = apiclient.post(
            reverse('patient-list'), data=patientd, format='json')
        # import ipdb; ipdb.set_trace()
        p = Patient.objects.get(pk=resp.data['pk'])
        [p.__dict__.pop(k) for k in ('id', '_state')]
        assert p.__dict__ == patientd
        assert resp.status_code == status.HTTP_201_CREATED

    def test_alive_is_default_on_create(self, apiclient, patientd):
        patientd['alive'] = False
        r = apiclient.post(reverse('patient-list'), data=patientd)
        p = Patient.objects.get(id=r.data['pk'])
        assert p.alive == True
