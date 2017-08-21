from string import capwords

from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


# cpitalyze first letter of name



class Patient(models.Model):
    """
    ase class of patient.&
    Require on ly 3 fields : name, firstname, birthdate
    """

    #required Field
    name = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    birthdate = models.DateField()

    #non required fields
    street = models.CharField(blank=True, max_length=200, default="")
    postalcode = models.CharField(blank=True, max_length=5, default="")
    city = models.CharField(max_length=200, blank=True, default="")
    phonenumber = models.CharField(blank=True, max_length=20, default="")
    email = models.EmailField(blank=True, max_length=100, default="")

    def __str__(self):
        """
        nice printing Firstname Name
        """
        return self.firstname + ' ' + self.name

    def save(self, *args, **kwargs):
        """
        customizing save method, adds :
        - fore capwords for name et firstanme
        """
        self.name = capwords(self.name)
        self.firstname = capwords(self.firstname)
        self.city = capwords(self.city)

        super(Patient, self).save(*args, **kwargs)
