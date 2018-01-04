from actes.serializers import ActeSerializer
from rest_framework import serializers

from .models import Conseil, LigneOrdonnance, Medicament, Ordonnance


class LigneOrdonnanceSerializer(serializers.ModelSerializer):
    """docstring for LigneOrdonnaceSerializer."""

    class Meta:
        model = LigneOrdonnance
        fields = ('ordonnance', 'pk', 'position')

    def create(self, validated_data):
        return self.Meta.model.objects.new_ligne(**validated_data)


class MedicamentSerializer(LigneOrdonnanceSerializer):
    """
    Serializer de base de pour chaque ligne d'ordonnance
    """

    class Meta:
        model = Medicament
        fields = LigneOrdonnanceSerializer.Meta.fields + (
            'cip',
            'nom',
            'posologie',
            'duree',
        )


class ConseilSerializer(LigneOrdonnanceSerializer):
    """
    Serializer de base de pour chaque ligne d'ordonnance
    """

    class Meta:
        model = Conseil
        fields = LigneOrdonnanceSerializer.Meta.fields + ('texte', )


class OrdonnanceSerializer(ActeSerializer):
    """
    Observation serializer
    """

    #url specifique to subclass : can't make it auto
    url = serializers.HyperlinkedIdentityField(view_name='ordonnance-detail')

    medicaments = MedicamentSerializer(many=True, read_only=True)
    conseils = ConseilSerializer(many=True, read_only=True)

    class Meta(ActeSerializer.Meta):
        model = Ordonnance
        fields = ActeSerializer.Meta.fields + ('medicaments', 'conseils')
