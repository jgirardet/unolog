from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

class UnoUser(AbstractUser):
    pass


"""

https://github.com/codingforentrepreneurs/srvup-rest-framework/blob/master/src/accounts/models.py
"""
