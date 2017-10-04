from django.shortcuts import render
from rest_framework import viewsets

from unologbase.models import Patient, Observation
from unologbase.serializers import PatientSerializer, ObservationSerializer

# Create your views here.


class PatientViewSet(viewsets.ModelViewSet):
    """
    base viewset for patients
    """
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class ObservationViewSet(viewsets.ModelViewSet):
    """
    base viewset for patients
    """
    queryset = Observation.objects.all()
    serializer_class = ObservationSerializer
