from rest_framework import viewsets

from .models import Observation
from .permissions import OnlyOwnerCanEdit
from .serializers import ObservationSerializer

# Create your views here.


class ObservationViewSet(viewsets.ModelViewSet):
    """
    base viewset for patients
    """
    queryset = Observation.objects.all()
    serializer_class = ObservationSerializer
    permission_classes = (OnlyOwnerCanEdit, )
