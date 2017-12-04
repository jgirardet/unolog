from rest_framework import serializers

from .models import Medic


class MedicSerializer(serializers.ModelSerializer):
    """
    Serializer de base de pour chaque ligne d'ordonnance
    """

    class Meta:
        model = Medic
        fields = (
            'cip',
            'nom',
            'posologie',
            'duree',
            'ald',
        )
