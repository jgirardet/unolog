from actes.serializers import ActeSerializer
from rest_framework import serializers

from .models import Conseil, LigneOrdonnance, Medicament, Ordonnance


class LigneOrdonnanceSerializer(serializers.HyperlinkedModelSerializer):
    """docstring for LigneOrdonnaceSerializer."""

    class Meta:
        model = LigneOrdonnance
        fields = ('url', 'ordonnance')

    def create(self, validated_data):
        return self.Meta.model.objects.new_ligne(**validated_data)

    def update(self, instance, validated_data):
        #ordonnance est read-only
        validated_data.pop('ordonnance')

        return super().update(instance, validated_data)

    def validate_ordonnance(self, data):
        if self.instance:
            ordo = self.instance.ordonnance.id
            return data['ordonnance']
            raise serializers.ValidationError("finish must occur after start")


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


class LigneRepresentationField(serializers.RelatedField):
    def to_representation(self, value):
        if isinstance(value, Medicament):
            ser = MedicamentSerializer(value)
            return ser.data


class OrdonnanceSerializer(ActeSerializer):
    """
    Observation serializer
    """

    #url specifique to subclass : can't make it auto
    url = serializers.HyperlinkedIdentityField(view_name='ordonnance-detail')

    lignes = serializers.SerializerMethodField()

    def get_lignes(self, obj):
        retour = []
        for ligne in obj.get_lignes():
            if isinstance(ligne, Medicament):
                ser = MedicamentSerializer(ligne, context=self.context)
                retour.append(ser.data)
            elif isinstance(ligne, Conseil):
                ser = ConseilSerializer(ligne, context=self.context)
                retour.append(ser.data)
        return retour

    class Meta(ActeSerializer.Meta):
        model = Ordonnance
        fields = ActeSerializer.Meta.fields + (
            'ordre',
            'lignes',
        )
