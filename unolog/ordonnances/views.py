from actes.views import ActeViewSet
from rest_framework import viewsets

from .models import Ordonnance
from .serializers import OrdonnanceSerializer


class OrdonnanceViewSet(ActeViewSet):
    """
    base viewset for Ordonances
    """
    queryset = Ordonnance.objects.all()
    serializer_class = OrdonnanceSerializer
