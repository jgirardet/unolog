from string import capwords

from django.db import models

CAPWORDS_ATTRS = ('name', 'firstname', 'city')


class PatientManager(models.Manager):
    """
    custum patient manger to modifie create and update
    """
    attrs = CAPWORDS_ATTRS

    # paremeter to capwords

    # def create_patient(self, name=None, firstname=None, birthdate=None):
    #     """
    #     every patient creatient must use this
    #     """
    #     if not name:
    #         raise ValueError('Must Include a name when adding a Patient')
    #     if not firstname:
    #         raise ValueError('Must Include a firstname when adding a Patient')
    #     if not birthdate:
    #         raise ValueError('Must Include a birthdate when adding a Patient')

    #     patient = self.model(
    #             name = name,
    #             firstname=  firstname,
    #             birthdate = birthdate
    #             )

    #     print('hello')
    #     patient.save(using=self.db)
    #     return patient

    def create(self, **kwargs):
        """
        enhancement
        """
        # capwors certain fields
        for i in self.attrs:
            kwargs[i] = capwords(kwargs[i])

        # recall base create
        return super(PatientManager, self).create(**kwargs)


class Patient(models.Model):
    """
    ase class of patient.&
    Require on ly 3 fields : name, firstname, birthdate
    """
    attrs = CAPWORDS_ATTRS
    # required Field
    name = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    birthdate = models.DateField()
    sexe = models.BooleanField(default=True)  #True if women else false
    # non required fields
    street = models.CharField(blank=True, max_length=200, default="")
    postalcode = models.CharField(blank=True, max_length=5, default="")
    city = models.CharField(max_length=200, blank=True, default="")
    phonenumber = models.CharField(blank=True, max_length=20, default="")
    email = models.EmailField(blank=True, max_length=100, default="")

    objects = PatientManager()

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
        for i in self.attrs:
            setattr(self, i, capwords(getattr(self, i)))

        super(Patient, self).save(*args, **kwargs)
