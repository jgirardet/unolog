import datetime
import random
from string import capwords

import pytest
from patients.models import Patient
from patients.serializers import PatientSerializer
from rest_framework import serializers
from rest_framework.reverse import reverse
from rest_framework.test import (APIClient, APIRequestFactory,
                                 force_authenticate)

pytestmark = pytest.mark.django_db


class TestPatientSerializer:
    """
    Class fort PatientSerializer testing
    """

    def test_check_birthdate(self, patientd):
        """
        check no bithdate later
        """

        d = datetime.date(3000, 1, 1)
        patientd['birthdate'] = d
        s = PatientSerializer(data=patientd)
        with pytest.raises(serializers.ValidationError):
            s.is_valid(raise_exception=True), "sould return validation error"

    def test_postal_code_max_size(self, patientd):
        patientd['postalcode'] = "123456"
        s = PatientSerializer(data=patientd)
        with pytest.raises(serializers.ValidationError):
            s.is_valid(raise_exception=True), " postale code can't be 6 digit"

    def test_postal_code_is_digit(self, patientd):
        patientd['postalcode'] = "aaaaa"
        s = PatientSerializer(data=patientd)
        with pytest.raises(serializers.ValidationError):
            s.is_valid(raise_exception=True), " postale code can't be chars"

    def test_phone_number_is_well_formated(self, patientd):
        a = patientd
        a['phonenumber'] = random.randrange(100000 - 88000)
        s = PatientSerializer(data=a)
        with pytest.raises(serializers.ValidationError):
            s.is_valid(raise_exception=True), " sould start with + or 0"
