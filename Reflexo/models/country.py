from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=255)
    phone_code = models.CharField(max_length=10)
    ISO2 = models.CharField(max_length=2)

    def __str__(self):
        return self.name


class CountryUser(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='users')


class CountryPatient(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='patients')


class CountryTherapist(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='therapists')
