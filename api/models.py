from django.db import models

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    address = models.CharField(max_length=200)
    num_tell = models.CharField(max_length=20)
    ville = models.CharField(max_length=200)
    centre = models.CharField(max_length=200)
    date_naissance = models.DateField()

class Maladie(models.Model):
    name = models.CharField(max_length=255)

class Prescriptions(models.Model):
    name = models.CharField(max_length=200)
    dosage = models.CharField(max_length=200)
    id_patient = models.ForeignKey(Patient,on_delete=models.CASCADE)

class Traitement(models.Model):
    id_patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    id_prescription = models.ForeignKey(Prescriptions,on_delete=models.CASCADE)

class EtatMaladie(models.Model):
    id_maladie = models.ForeignKey(Maladie,on_delete=models.CASCADE)
    id_traitement = models.ForeignKey(Traitement,on_delete=models.CASCADE)
    status = models.CharField(max_length=200)