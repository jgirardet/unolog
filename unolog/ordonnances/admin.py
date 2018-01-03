from django.contrib import admin

from .models import LigneOrdonnance, Medicament, Ordonnance

# Register your models here.

admin.site.register(Ordonnance)
# admin.site.register(LigneOrdonnance)
admin.site.register(Medicament)
# admin.site.register(Conseil)
