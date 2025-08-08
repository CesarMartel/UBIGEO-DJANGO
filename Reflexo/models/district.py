from django.db import models
from .province import Province  # <-- este import es clave


class District(models.Model):
    province = models.ForeignKey(
        Province,
        on_delete=models.CASCADE,
        related_name="districts"  # este es el nombre para acceder desde Province
    )


class DistrictUser(models.Model):
    name = models.CharField(max_length=255)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='users')

    def __str__(self):
        return self.name


class DistrictPatient(models.Model):
    name = models.CharField(max_length=255)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='patients')

    def __str__(self):
        return self.name
    

class DistrictTherapist(models.Model):
    name = models.CharField(max_length=255)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='therapists')

    def __str__(self):
        return self.name
