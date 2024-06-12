from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
from .models import Car, Brand, Color
from .serializers import CarSerializer, ColorSerializer, BrandSerializer

'''old one'''

# class CarAPIview(ListCreateAPIView):
#     queryset = Car.objects.filter(published=True)
#     serializer_class = CarSerializer
#
#
# class CarAPIDetail(RetrieveAPIView):
#     queryset = Car.objects.filter(published=True)
#     serializer_class = CarSerializer

'''new one'''


class CarApiView(APIView):
    def get(self, request: Request) -> Response:
        cars = Car.objects.all()
        return Response(CarSerializer(cars, many=True).data)

    def post(self, request: Request) -> Response:
        name = request.data['name']
        brand = request.data['brand']
        color = request.data['color']
        speed = request.data['speed']
        price = request.data['price']
        created = request.data['created']
        published = request.data['published']

        car = Car.objects.create(
            name=name,
            brand=brand,
            color=color,
            speed=speed,
            price=price,
            created=created,
            published=published,

        )
        return Response({'car': model_to_dict(car), 'message': 'car created'})

'''old one'''
# class ColorAPIView(ListCreateAPIView):
#     queryset = Color.objects.all()
#     serializer_class = ColorSerializer
#
#
# class ColorAPIDetail(RetrieveAPIView):
#     queryset = Color.objects.all()
#     serializer_class = ColorSerializer

'''new one'''


class ColorAPIView(APIView):
    def get(self, request: Request) -> Response:
        colors = Color.objects.all()
        return Response(ColorSerializer(colors, many=True).data)

    def post(self, request: Request) -> Response:
        name = request.data['name']
        created = request.data['created']
        published = request.data['published']

        color = Color.objects.create(
            name=name,
            created=created,
            published=published,
        )
        return Response({'color': model_to_dict(color), 'message': 'color created'})


'''old one'''
# class BrandAPIView(ListCreateAPIView):
#     queryset = Brand.objects.all()
#     serializer_class = BrandSerializer
#
#
# class BrandAPIDetail(RetrieveAPIView):
#     queryset = Brand.objects.all()
#     serializer_class = BrandSerializer

'''new one'''


class BrandAPIView(APIView):
    def get(self, request: Request) -> Response:
        brand = Brand.objects.all()
        return Response(BrandSerializer(brand, many=True).data)

    def post(self, request: Request) -> Response:
        name = request.data['name']
        created = request.data['created']
        published = request.data['published']

        brand = Brand.objects.create(
            name=name,
            created=created,
            published=published,
        )
        return Response({'brand': model_to_dict(brand), 'message': 'brand created'})

