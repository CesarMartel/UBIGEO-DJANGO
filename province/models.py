from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Province(models.Model):
    name = models.CharField(max_length=255)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    # Relaciones
    users = models.ManyToManyField('User')
    patients = models.ManyToManyField('Patient')
    therapists = models.ManyToManyField('Therapist')
    districts = models.ManyToManyField('District')

    class Meta:
        verbose_name = "Province"
        verbose_name_plural = "Provinces"

    def __str__(self):
        return self.name
