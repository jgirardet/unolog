from rest_framework import serializers

from actes.models import Observation


class ObservationSerializer(serializers.ModelSerializer):
    """
    Observation serializer
    """

    class Meta:
        model = Observation
        fields = '__all__'
