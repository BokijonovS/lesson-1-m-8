from django.db import models


# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=35, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "1. Brand."


class Color(models.Model):
    name = models.CharField(max_length=20, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "2. Colors."


class Car(models.Model):
    name = models.CharField(max_length=40)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True)
    speed = models.IntegerField()
    price = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "3. Cars."
