from django.shortcuts import render

# Create your views here.
from .models import Car, Brand, Color
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from .serializers import CarSerializer, ColorSerializer, BrandSerializer


class CarAPIview(ListCreateAPIView):
    queryset = Car.objects.filter(published=True)
    serializer_class = CarSerializer


class CarAPIDetail(RetrieveAPIView):
    queryset = Car.objects.filter(published=True)
    serializer_class = CarSerializer


class ColorAPIView(ListCreateAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class ColorAPIDetail(RetrieveAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class BrandAPIView(ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class BrandAPIDetail(RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
