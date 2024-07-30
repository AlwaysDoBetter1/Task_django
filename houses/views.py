from rest_framework import viewsets
from .models import House, Entrance, Apartment
from .serializers import HouseSerializer, EntranceSerializer, ApartmentSerializer

class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer

class EntranceViewSet(viewsets.ModelViewSet):
    queryset = Entrance.objects.all()
    serializer_class = EntranceSerializer

class ApartmentViewSet(viewsets.ModelViewSet):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer