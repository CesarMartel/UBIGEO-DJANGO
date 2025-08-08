from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=255)

    # Campos para soft delete
    deleted_at = models.DateTimeField(null=True, blank=True)

    def delete(self, using=None, keep_parents=False):
        """Soft delete: solo marca como eliminado sin borrar de la BD."""
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        """Restaura un registro eliminado."""
        self.deleted_at = None
        self.save()

    # Relaciones
    def users(self):
        return self.user_set.all()  # Django crea relación inversa por defecto

    def patients(self):
        return self.patient_set.all()

    def therapists(self):
        return self.therapist_set.all()

    def provinces(self):
        return self.province_set.all()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "region"
