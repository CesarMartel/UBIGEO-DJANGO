from django.db import models
from .region import Region

class Province(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, related_name='provinces', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ProvinceUser(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='users')
    # otros campos...


class ProvincePatient(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='patients')
    # otros campos...


class ProvinceTherapist(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='therapists')
    # otros campos...


class ProvinceDistrict(models.Model):
    province = models.ForeignKey(
        Province,
        on_delete=models.CASCADE,
        related_name="province_districts"  # nombre distinto
    )