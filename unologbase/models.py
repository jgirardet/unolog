from string import capwords

from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


# cpitalyze first letter of name


class PatientManager(models.Manager):
    """
manager for Patient Class
    """

    def create(self, name, firstname, birthdate):
        """
Every new patient is created via this method
Name : always saved as capword
Firstname : always saved as capword
"""
        patient = Patient(
            name=capwords(name),
            firstname=capwords(firstname),
            birthdate=birthdate, )
        patient.clean()
        patient.save()
        return patient


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
    street = models.CharField(blank=True, max_length=200)
    postalcode = models.IntegerField(max_length=5, blank=True)
    city = models.CharField(max_length=200, blank=True)
    tel_number = models.IntegerField(blank=True)

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

        super(Patient, self).save(*args, **kwargs)
