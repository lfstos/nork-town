from rest_framework.exceptions import ValidationError
from rest_framework import generics
from .models import Car, Owner
from .serializers import OwnerSerializer, CarSerializer


class CarListCreateView(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def perform_create(self, serializer):
        owner = serializer.validated_data['owner']
        if owner.car_count >= 3:
            raise ValidationError("Proprietário já possui 3 carros.")
        owner.increment_car_count()
        owner.save()


class CarRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class OwnerListCreateView(generics.ListCreateAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer


class OwnerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
