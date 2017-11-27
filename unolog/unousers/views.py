from rest_framework import viewsets

from .models import UnoUser
from .serializers import UnoUserSerializer

# Create your views here.


class UnoUserViewSet(viewsets.ModelViewSet):
    """
    base viewset for patients
    """
    queryset = UnoUser.objects.all()
    serializer_class = UnoUserSerializer
