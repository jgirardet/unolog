from actes.views import ActeViewSet
from rest_framework import viewsets

from .models import Conseil, Medicament, Ordonnance
from .permissions import OnlyOwnerCanEditLigneOrdonnance
from .serializers import (ConseilSerializer, MedicamentSerializer,
                          OrdonnanceSerializer)


class OrdonnanceViewSet(ActeViewSet):
    """
    base viewset for Ordonances
    """
    queryset = Ordonnance.objects.all()
    serializer_class = OrdonnanceSerializer


class LigneViewset(viewsets.ModelViewSet):
    """
    view set for ligne ordonnance
    """

    permission_classes = (OnlyOwnerCanEditLigneOrdonnance, )

    # def perform_create(self, serializer):
    #     """
    #     add user to owner saving instance
    #     """
    #     serializer.save(owner=self.request.user)


class MedicamentViewset(LigneViewset):
    """
    view set for ligne ordonnance
    """
    queryset = Medicament.objects.all()
    serializer_class = MedicamentSerializer
    permission_classes = (OnlyOwnerCanEditLigneOrdonnance, )


class ConseilViewset(LigneViewset):
    """
    view set for ligne ordonnance
    """
    queryset = Conseil.objects.all()
    serializer_class = ConseilSerializer
