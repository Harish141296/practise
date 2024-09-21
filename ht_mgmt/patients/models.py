from django.db import models

# Create your models here.
class Patient(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=30)
    dob = models.DateTimeField()
    gender = models.CharField(max_length=20)
    phonenumber = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete = models.CASCADE)
    appointment_date = models.DateTimeField()
    reason = models.TextField()

    def __str__(self):
        return f"Appointment for {self.patient} on {self.appointment_date}"
    


