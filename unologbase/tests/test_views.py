import pytest
# from django.contrib.auth import get_user_model
# from django.contrib.auth.models import AnonymousUser, User
# from hypothesis import strategies as st, settings
# from hypothesis import assume, given
from mixer.backend.django import Mixer, mixer
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import (APIClient, APIRequestFactory,
                                 force_authenticate)
from unologbase.models import Patient
from unologbase.serializers import PatientSerializer
from unologbase.views import PatientViewSet

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
        ser = PatientSerializer(patients, many=True)
        assert resp.data == ser.data

    def test_response_create_patient(self, apiclient, patient_nodb):

        resp = apiclient.post(
            reverse('patient-list'), patient_nodb.__dict__, format='json')
        p = Patient.objects.get(pk=resp.data['pk'])
        [p.__dict__.pop(k) for k in ('id', '_state')]
        assert p.__dict__ == patient_nodb.__dict__
        assert resp.status_code == status.HTTP_201_CREATED
