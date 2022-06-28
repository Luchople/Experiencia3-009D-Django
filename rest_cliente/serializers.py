from rest_framework import serializers
from core.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'rut', 'correo', 'telefono', 'direccion']
