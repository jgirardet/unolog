from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from string import capwords
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
			name = capwords(name),
			firstname = capwords(firstname),
			birthdate = birthdate,
			)
		patient.clean()
		patient.save()
		return patient





class Patient(models.Model):
	"""
	Base class of patient.&
	Require on ly 3 fields : name, firstname, birthdate
	"""

	name = models.CharField(max_length=50)
	firstname = models.CharField(max_length=50)
	birthdate = models.DateField()
	street = models.CharField(blank=True, max_length=200)

	
	def __str__(self):
		"""
		nice printing Firstname Name
		"""
		return self.firstname+' '+self.name


	def save(self, *args, **kwargs):
		"""
		customizing save method, adds :
		 - fore capwords for name et firstanme
		"""
		self.name = capwords(self.name)
		self.firstname = capwords(self.firstname)

		super(Patient, self).save(*args, **kwargs)