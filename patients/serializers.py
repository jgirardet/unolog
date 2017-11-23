import datetime
from string import capwords

from rest_framework import serializers

from patients.models import Patient


class PatientSerializer(serializers.ModelSerializer):
    """
    Serializer of patient model
    """

    class Meta:

        model = Patient
        fields = (
            'pk',
            'name',
            'firstname',
            'birthdate',
            'sexe',
            'street',
            'postalcode',
            'city',
            'phonenumber',
            'email', )

    def validate_birthdate(self, value):
        """
        check birthdate not in future
        """
        if value > datetime.date.today():
            raise serializers.ValidationError(
                "patient can't be born in future Mr Conor")

        return value

    def validate_postalcode(self, value):
        """
        check postalcode is only numeric
        """
        if value and not value.isdigit():
            raise serializers.ValidationError("postal code must be digit only")
        return value

    def validate_phonenumber(self, value):
        """
        check phone number starts with 0 or +
        """
        if value and value[0] not in ['0', '+']:
            raise serializers.ValidationError(
                "phone number must starts with 0 or +")
        return value

    # def create(self, validated_data):
    #   """
    #   custom create for PatientSerializer
    #   """

    #   #automatique capwords name and firstanme
    #   validated_data['name'] = capwords(validated_data['name'])
    #   validated_data['firstname'] = capwords(validated_data['firstname'])

    #   patient = Patient.objects.create(**validated_data)
    #   return patient
