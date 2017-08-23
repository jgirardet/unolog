"""
here we import all models
"""
from django.db import models

from .patients import Patient
from .actes import Observation
from .users import UnoUser

from django.contrib.auth import get_user_model
User = get_user_model()
