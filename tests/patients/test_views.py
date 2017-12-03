from string import capwords

import pytest
from mixer.backend.django import mixer
# from django.contrib.auth import get_user_model
# from django.contrib.auth.models import AnonymousUser, User
# from hypothesis import strategies as st, settings
# from hypothesis import assume, given
from patients.models import Patient
from patients.serializers import PatientSerializer
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIRequestFactory

# from conftest import apiclient

# LeUser = get_user_model()

pytestmark = pytest.mark.django_db


# @pytest.mark.usefixtures("apiclient")
class TestPatientView:
    """"
Base classe fo testing patient views
"""

    def test_retrieve_patient_list(self, apiclient):

        patients = mixer.cycle(20).blend(Patient)
        resp = apiclient.get(reverse('patient-list'))
        patients = Patient.objects.all()
        req = APIRequestFactory().get(reverse('patient-list'))
        ser = PatientSerializer(patients, many=True, context={'request': req})
        assert resp.data == ser.data

    def test_response_create_patient(self, apiclient, patient_dict):

        for i in Patient.attrs:  #turn capsword what is not saved
            patient_dict[i] = capwords(patient_dict[i])

        resp = apiclient.post(
            reverse('patient-list'), data=patient_dict, format='json')
        # import ipdb; ipdb.set_trace()
        p = Patient.objects.get(pk=resp.data['pk'])
        [p.__dict__.pop(k) for k in ('id', '_state')]
        assert p.__dict__ == patient_dict
        assert resp.status_code == status.HTTP_201_CREATED

    def test_caps_test(self, apiclient, patient_dict):
        patient_dict['name'] = "Rebecca Ramirez DDS"
        for i in Patient.attrs:
            patient_dict[i] = capwords(patient_dict[i])

        resp = apiclient.post(
            reverse('patient-list'), data=patient_dict, format='json')
        # import ipdb; ipdb.set_trace()
        p = Patient.objects.get(pk=resp.data['pk'])
        [p.__dict__.pop(k) for k in ('id', '_state')]
        assert p.__dict__ == patient_dict
        assert resp.status_code == status.HTTP_201_CREATED

    def test_alive_is_default_on_create(self, apiclient, patient_dict):
        patient_dict['alive'] = False
        r = apiclient.post(reverse('patient-list'), data=patient_dict)
        p = Patient.objects.get(id=r.data['pk'])
        assert p.alive == True
