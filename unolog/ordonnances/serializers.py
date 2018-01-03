from actes.serializers import ActeSerializer
from rest_framework import serializers

from .models import Conseil, LigneOrdonnance, Medicament, Ordonnance


class LigneOrdonnanceSerializer(serializers.ModelSerializer):
    """docstring for LigneOrdonnaceSerializer."""

    ordre = serializers.CharField(source = 'ordonnance.ordre', read_only=True)

    class Meta:
        model = LigneOrdonnance
        fields = ('ordonnance', 'pk', 'position','ordre')

class MedicamentSerializer(LigneOrdonnanceSerializer):
    """
    Serializer de base de pour chaque ligne d'ordonnance
    """

    class Meta:
        model = Medicament
        fields =  LigneOrdonnanceSerializer.Meta.fields + ('cip','nom','posologie','duree',)


class ConseilSerializer(LigneOrdonnanceSerializer):
    """
    Serializer de base de pour chaque ligne d'ordonnance
    """

    class Meta:
        model = Conseil
        fields =  LigneOrdonnanceSerializer.Meta.fields + ('texte',)




class OrdonnanceSerializer(ActeSerializer):
    """
    Observation serializer
    """

    url = serializers.HyperlinkedIdentityField(view_name='ordonnance-detail')
    medicaments = MedicamentSerializer(many=True, read_only=True)
    conseils = ConseilSerializer(many=True, read_only=True)

    class Meta(ActeSerializer.Meta):
        model = Ordonnance
        fields = ActeSerializer.Meta.fields + ('ordre','medicaments', 'conseils' )
