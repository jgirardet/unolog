from rest_framework import serializers

from .models import UnoUser


class UnoUserSerializer(serializers.ModelSerializer):
    """
    Observation serializer
    """

    class Meta:
        model = UnoUser
        fields = ("username", "pk", "statut")

    #def validate
