from rest_framework import serializers
from cliente.models import Customer

#aqui se crea el serializador de cliente
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields='__all__'
        

