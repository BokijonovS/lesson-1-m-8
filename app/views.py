from django.shortcuts import render
from rest_framework.views import APIView

# Create your views here.
from .models import Car, Brand, Color
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from .serializers import CarSerializer, ColorSerializer, BrandSerializer
from rest_framework.request import Request
from rest_framework.response import Response
from django.forms import model_to_dict

# class CarAPIview(ListCreateAPIView):
#     queryset = Car.objects.filter(published=True)
#     serializer_class = CarSerializer


class CarAPIview(APIView):
    def get(self, request: Request):
        cars = Car.objects.all()
        return Response({"cars": CarSerializer(cars, many=True).data})

    def post(self, request: Request):
        car = Car.objects.create(
            name=request.data['name'],
            brand_id=request.data['brand_id'],
            color_id=request.data['color_id'],
            speed=request.data['speed'],
            price=request.data['price']
        )
        return Response({'car': model_to_dict(car), 'message': 'Car created!'})

class CarAPIDetail(RetrieveAPIView):
    queryset = Car.objects.filter(published=True)
    serializer_class = CarSerializer


# class ColorAPIView(ListCreateAPIView):
#     queryset = Color.objects.all()
#     serializer_class = ColorSerializer

class ColorAPIView(APIView):
    def get(self, request: Request):
        colors = Color.objects.all()
        return Response({"colors": ColorSerializer(colors, many=True).data})

    def post(self, request: Request):
        color = Color.objects.create(
            name=request.data['name']
        )
        return Response({'color': model_to_dict(color), 'message': 'Color created!'})


class ColorAPIDetail(RetrieveAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


# class BrandAPIView(ListCreateAPIView):
#     queryset = Brand.objects.all()
#     serializer_class = BrandSerializer

class BrandAPIView(APIView):
    def get(self, request: Request):
        brands = Brand.objects.all()
        return Response({"brands": BrandSerializer(brands, many=True).data})

    def post(self, request: Request):
        brand = Brand.objects.create(
            name=request.data['name']
        )
        return Response({'brand': model_to_dict(brand), 'message': 'Brand created!'})


class BrandAPIDetail(RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
