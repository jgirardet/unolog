from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UnoUser

admin.site.register(UnoUser, UserAdmin)