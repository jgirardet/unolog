from rest_framework import viewsets

from .models import Medic
from .serializers import MedicSerializer


class MedicViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour chaque ligne d'ordonnance
    """

    queryset = Medic.objects.all()
    serializer_class = MedicSerializer
