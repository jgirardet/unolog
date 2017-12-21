from actes.serializers import ActeSerializer
from rest_framework import serializers

from .models import Medicament, Ordonnance


class MedicamentSerializer(serializers.ModelSerializer):
    """
    Serializer de base de pour chaque ligne d'ordonnance
    """

    class Meta:
        model = Medicament
        fields = ('position', )


class OrdonnanceSerializer(ActeSerializer):
    """
    Observation serializer
    """

    url = serializers.HyperlinkedIdentityField(view_name='ordonnance-detail')

    medics = MedicamentSerializer(many=True, read_only=True)

    class Meta(ActeSerializer.Meta):
        model = Ordonnance
        fields = ActeSerializer.Meta.fields + ('medics', )
