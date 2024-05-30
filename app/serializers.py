from rest_framework import serializers

from .models import Car, Color, Brand


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


# second part of the task


# def deserialization():
#     json = b'{"name":"test","content":"test content"}'
#     stream = io.BytesIO(json)
#     data = JSONParser().parse(stream)
#     print(data, "Json parser object")
#
#     serializer = NewSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
#
#
# def serialization():
#     news1 = News("test", "test content")
#     serializer = NewSerializer(news1)
#     print(serializer.data)
#
#     json = JSONRenderer().render(serializer.data)
#     print(json)
#     print(type(json))
