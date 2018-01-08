from rest_framework import mixins, viewsets

from .models import Observation
from .permissions import OnlyOwnerCanEdit
from .serializers import ObservationSerializer


class ActeViewSet(viewsets.ModelViewSet):
    """ base common viewset for ActeS
    """
    permission_classes = (OnlyOwnerCanEdit, )

    def perform_create(self, serializer):
        """
        add user to owner saving instance
        """
        serializer.save(owner=self.request.user)


class ObservationViewSet(ActeViewSet):
    """
    base viewset for patients
    """
    queryset = Observation.objects.all()
    serializer_class = ObservationSerializer
