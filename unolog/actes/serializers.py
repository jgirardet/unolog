from actes.models import Observation
from patients.models import Patient
from rest_framework import serializers


class ActeSerializer(serializers.HyperlinkedModelSerializer):
    """
    BaseActe serializer
    """

    pk = serializers.IntegerField(label='ID', read_only=True)
    patient = serializers.HyperlinkedRelatedField(
        queryset=Patient.objects.all(),
        view_name='patient-detail',
    )
    created = serializers.DateTimeField(read_only=True)
    modified = serializers.DateTimeField(read_only=True)
    owner = serializers.HyperlinkedRelatedField(
        view_name='unouser-detail', read_only=True)

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
    url = serializers.HyperlinkedIdentityField(view_name='observation-detail')

    class Meta(ActeSerializer.Meta):
        model = Observation
        fields = ActeSerializer.Meta.fields + ('motif', 'body')
