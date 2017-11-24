from actes.models import Observation
from patients.models import Patient
from rest_framework import serializers
from unousers.models import UnoUser


class ActeSerializer(serializers.HyperlinkedModelSerializer):
    """
    BaseActe serializer
    """
    url = serializers.HyperlinkedIdentityField(view_name='observation-detail')
    pk = serializers.IntegerField(label='ID', read_only=True)
    patient = serializers.HyperlinkedRelatedField(
        queryset=Patient.objects.all(),
        view_name='patient-detail',
    )
    created = serializers.DateTimeField(read_only=True)
    modified = serializers.DateTimeField(read_only=True)
    owner = serializers.HyperlinkedRelatedField(
        queryset=UnoUser.objects.all(), view_name='unouser-detail')

    class Meta:
        fields = (
            'url',
            'pk',
            'patient',
            'created',
            'modified',
            'owner',
        )


class ObservationSerializer(ActeSerializer):
    """
    Observation serializer
    """

    class Meta(ActeSerializer.Meta):
        model = Observation
        fields = ActeSerializer.Meta.fields + ('motif', 'body')
