from rest_framework import viewsets

from actes.models import Observation
from actes.serializers import ObservationSerializer

# Create your views here.


class ObservationViewSet(viewsets.ModelViewSet):
    """
    base viewset for patients
    """
    queryset = Observation.objects.all()
    serializer_class = ObservationSerializer
