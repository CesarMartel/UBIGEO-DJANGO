from rest_framework import serializers
from .models import Province, Region

class ProvinceSerializer(serializers.ModelSerializer):
    # Puedes personalizar la forma en que los campos se serializan si es necesario
    region = serializers.StringRelatedField()  # Serializa la región como una cadena

    class Meta:
        model = Province
        fields = ['id', 'name', 'region', 'users', 'patients', 'therapists', 'districts']
