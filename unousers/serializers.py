from rest_framework import serializers

from .models import UnoUser


class UnoUserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Observation serializer
    """

    class Meta:
        model = UnoUser
        fields = ("username", "pk", "observations")
