from rest_framework import viewsets

from patients.models import Patient
from patients.serializers import PatientSerializer

# Create your views here.


class PatientViewSet(viewsets.ModelViewSet):
    """
    base viewset for patients
    """
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
