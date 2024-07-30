from rest_framework import serializers
from .models import House, Entrance, Apartment

class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = '__all__'

class EntranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrance
        fields = '__all__'

class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = '__all__'