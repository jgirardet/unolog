from actes.views import ActeViewSet
from rest_framework import viewsets

from .models import Conseil, Medicament, Ordonnance
from .serializers import (ConseilSerializer, LigneOrdonnanceSerializer,
                          MedicamentSerializer, OrdonnanceSerializer)


class OrdonnanceViewSet(ActeViewSet):
    """
    base viewset for Ordonances
    """
    queryset = Ordonnance.objects.all()
    serializer_class = OrdonnanceSerializer


#
# class LigneOrdonnanceViewset(viewsets.ModelViewSet):
#     """
#     view set for ligne ordonnance
#     """
#     queryset = LigneOrdonnance.objects.all()
#     serializer_class = LigneOrdonnanceSerializer
#


class MedicamentViewset(viewsets.ModelViewSet):
    """
    view set for ligne ordonnance
    """
    queryset = Medicament.objects.all()
    serializer_class = MedicamentSerializer


class ConseilViewset(viewsets.ModelViewSet):
    """
    view set for ligne ordonnance
    """
    queryset = Conseil.objects.all()
    serializer_class = ConseilSerializer
