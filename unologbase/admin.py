from django.contrib import admin
from django.contrib.auth import get_user_model
from unologbase.models import (
        Patient,
        Observation,
        )
# Register your models here.

User = get_user_model()

admin.site.register(User)
admin.site.register(Patient)
admin.site.register(Observation)
