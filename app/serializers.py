import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Car, Color, Brand


class CarSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    brand_id = serializers.IntegerField()
    color_id = serializers.IntegerField()
    speed = serializers.IntegerField()
    price = serializers.IntegerField()
    created = serializers.DateTimeField(read_only=True)
    published = serializers.BooleanField(default=True)




class ColorSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    created = serializers.DateTimeField(read_only=True)
    published = serializers.BooleanField(default=True)


class BrandSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    created = serializers.DateTimeField(read_only=True)
    published = serializers.BooleanField(default=True)


# def serialization():
#     car1 = Car(name="Car1", brand_id=1)
#     serializer = CarSerializer(car1)
#
#     json = JSONRenderer().render(serializer.data)
#     print(json)
#
#
# def deserialization():
#     json = b'{"name":"nimadir","brand_id":1,"color_id":1,"speed":1,"price":1}'
#     stream = io.BytesIO(json)
#     data = JSONParser().parse(stream)
#     print(data, 'Json parser objekti')
#
#     serializer = CarSerializer(data)
#     serializer.is_valid(raise_exception=True)
#     print(serializer.validated_data)


