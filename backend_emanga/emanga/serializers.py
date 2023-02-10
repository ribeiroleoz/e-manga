from rest_framework import serializers
from emanga.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cliente
        fields=('id', 'nome')