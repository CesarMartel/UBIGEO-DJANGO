from django.db import models

class Province(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'Reflexo'


class District(models.Model):
    name = models.CharField(max_length=255)
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='districts')

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'Reflexo'


class DistrictUser(models.Model):
    name = models.CharField(max_length=255)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='users')

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'Reflexo'


class DistrictPatient(models.Model):
    name = models.CharField(max_length=255)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='patients')

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'Reflexo'


class DistrictTherapist(models.Model):
    name = models.CharField(max_length=255)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='therapists')

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'Reflexo'
