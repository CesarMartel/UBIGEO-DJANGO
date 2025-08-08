from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=255)
    phone_code = models.CharField(max_length=10)
    ISO2 = models.CharField(max_length=2)

    def __str__(self):
        return self.name


class User(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='users')
    # otros campos de usuario...


class Patient(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='patients')
    # otros campos de paciente...


class Therapist(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='therapists')
    # otros campos de terapeuta...
