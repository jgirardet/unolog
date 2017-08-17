from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.

from unologbase.models import Patient
from unologbase.serializers import PatientSerializer

class PatientViewSet(viewsets.ModelViewSet):
	"""
	base viewset for patients
	"""
	queryset = Patient.objects.all()
	serializer_class = PatientSerializer
