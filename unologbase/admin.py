from django.contrib import admin

from .models import Observation, Patient

admin.site.register(Patient)
admin.site.register(Observation)
