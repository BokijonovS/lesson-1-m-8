from django.contrib import admin

# Register your models here.
from .models import Color, Brand, Car


@admin.register(Color, Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'created', 'published')
    list_display_links = ('pk', 'name')


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'brand', 'color', 'speed', 'price', 'created', 'published')
    list_display_links = ('pk', 'name')
