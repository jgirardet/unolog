from rest_framework import serializers

from actes.models import Observation


class ObservationSerializer(serializers.HyperlinkedModelSerializer):
    """
    Observation serializer
    """

    class Meta:
        model = Observation
        fields = ('url', 'pk', 'patient', 'created', 'modified', 'owner',
                  'motif', 'body')
