from actes.serializers import ActeSerializer
from rest_framework import serializers

from .models import Conseil, LigneOrdonnance, Medicament, Ordonnance


class MedicamentSerializer(serializers.ModelSerializer):
    """
    Serializer de base de pour chaque ligne d'ordonnance
    """

    class Meta:
        model = Medicament
        fields = (
            'cip',
            'nom',
            'posologie',
            'duree',
            # 'ligne',
        )


class ConseilSerializer(serializers.ModelSerializer):
    """
    Serializer de base de pour chaque ligne d'ordonnance
    """

    class Meta:
        model = Conseil
        fields = ('texte', )


class TypeRelatedField(serializers.RelatedField):
    # def get_queryset(self):
    #     return value.objects.all()

    def to_representation(self, value):
        if isinstance(value, Medicament):
            serializer = MedicamentSerializer(value)
            letype = Medicament
        elif isinstance(value, Conseil):
            serializer = ConseilSerializer(value)
            letype = Conseil
        else:
            raise Exception('Unexpected type of tagged object')

        return serializer.data

    def to_internal_value(self, data):
        # you need to pass some identity to figure out which serializer to use
        # supose you'll add 'meeting_type' key to your json
        letype = data.pop('content_type')
        print(letype)

        if meeting_type == 'medicament':
            serializer = MedicamentSerializer(data)
        elif meeting_type == 'conseil':
            serializer = ConseilSerializer(data)
        else:
            raise serializers.ValidationError('no ligne type provided')

        if serializer.is_valid():
            obj = serializer.save()
        else:
            raise serializers.ValidationError(serializer.errors)

        return obj


class LigneOrdonnanceSerializer(serializers.ModelSerializer):
    """
    ligne ordonnace serializer
    """

    content_type = serializers.CharField(source='content_type.name')
    contenu = TypeRelatedField(queryset=content_type.model.objects.all())

    class Meta:
        model = LigneOrdonnance
        fields = ('pk', 'position', 'ald', 'contenu', 'content_type')


class OrdonnanceSerializer(ActeSerializer):
    """
    Observation serializer
    """

    url = serializers.HyperlinkedIdentityField(view_name='ordonnance-detail')
    lignes = LigneOrdonnanceSerializer()

    class Meta(ActeSerializer.Meta):
        model = Ordonnance
        fields = ActeSerializer.Meta.fields + ('lignes', )
