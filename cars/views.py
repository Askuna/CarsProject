from django.shortcuts import render
from requests import Response
from rest_framework import generics
from rest_framework.decorators import api_view

from cars.serializers import CarDetailSerializer, CarsListSerializer
from cars.models import Car
from cars.permissions import  IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from  rest_framework.authentication import TokenAuthentication
from rest_framework.reverse import reverse
# Create your views here.

class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer


class CarsListView(generics.ListAPIView):
    serializer_class = CarsListSerializer
    queryset = Car.objects.all()
    permission_classes = (IsAdminUser,)


class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarDetailSerializer
    queryset = Car.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsOwnerOrReadOnly,)

# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'cars': reverse('cars-list', request=request, format=format),
#     })

