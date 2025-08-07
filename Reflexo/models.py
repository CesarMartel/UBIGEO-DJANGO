from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)
    phone_code = models.CharField(max_length=10)
    ISO2 = models.CharField(max_length=2)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name
