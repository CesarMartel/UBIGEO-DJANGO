from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=255)
    phone_code = models.CharField(max_length=10)
    ISO2 = models.CharField(max_length=2)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'Reflexo'


class CountryUser(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='users')

    class Meta:
        app_label = 'Reflexo'


class CountryPatient(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='patients')

    class Meta:
        app_label = 'Reflexo'


class CountryTherapist(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='therapists')

    class Meta:
        app_label = 'Reflexo'
