from rest_framework import serializers, viewsets
from  .models import Dht
class Dhtserializer(serializers.ModelSerializer):
    class Meta :
        model = Dht
        fields = ['id', 'temp', 'dt']