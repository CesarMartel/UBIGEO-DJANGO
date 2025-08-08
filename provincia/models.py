from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=100)

class Province(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, related_name='provinces', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def users(self):
        return self.user_set.all()

    def patients(self):
        return self.patient_set.all()

    def therapists(self):
        return self.therapist_set.all()

    def districts(self):
        return self.district_set.all()
