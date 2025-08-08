from django.db import models
from django.utils import timezone

class Region(models.Model):
    name = models.CharField(max_length=255)

    deleted_at = models.DateTimeField(null=True, blank=True)

    def delete(self, using=None, keep_parents=False):
        """Soft delete."""
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        """Restaura un registro eliminado."""
        self.deleted_at = None
        self.save()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "region"


class RegionUser(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='users')
    # otros campos...


class RegionPatient(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='patients')
    # otros campos...


class RegionTherapist(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='therapists')
    # otros campos...
