from patients.models import Patient
from patients.serializers import PatientSerializer
from rest_framework import viewsets

# Create your views here.


class PatientViewSet(viewsets.ModelViewSet):
    """
    base viewset for patients
    """
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def perform_create(self, serializer):
        """
        alive should always be True
        """
        serializer.save(alive=True)
