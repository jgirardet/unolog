import datetime
import random
from string import capwords

import pytest
from mixer.backend.django import Mixer, mixer
from rest_framework import serializers
from rest_framework.reverse import reverse
from rest_framework.test import (APIClient, APIRequestFactory,
                                 force_authenticate)

from patients.models import Patient
from patients.serializers import PatientSerializer

pytestmark = pytest.mark.django_db


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

    def test_postal_code_max_size(self, patient_dict):
        patient_dict['postalcode'] = "123456"
        s = PatientSerializer(data=patient_dict)
        with pytest.raises(serializers.ValidationError):
            s.is_valid(raise_exception=True), " postale code can't be 6 chars"

    def test_phone_number_is_well_formated(self, patient_dict):
        a = patient_dict
        a['phonenumber'] = random.randrange(100000 - 88000)
        s = PatientSerializer(data=a)
        with pytest.raises(serializers.ValidationError):
            s.is_valid(raise_exception=True), " sould start with + or 0"

    def test_fix(self, apiclient):
        r = apiclient.get('/api')
        assert r.status_code == 404