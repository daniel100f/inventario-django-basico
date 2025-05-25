from rest_framework import viewsets
from cliente.api.serializer import CustomerSerializer
from cliente.models import Customer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer





