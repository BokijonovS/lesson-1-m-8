"""
URL configuration for cars project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import CarAPIview, CarAPIDetail, BrandAPIView, BrandAPIDetail, ColorAPIView, ColorAPIDetail

urlpatterns = [
    path('admin/', admin.site.urls),

    path('hometask/brand/', BrandAPIView.as_view()),
    path('hometask/brand/<int:pk>/', BrandAPIDetail.as_view()),

    path('hometask/color/', ColorAPIView.as_view()),
    path('hometask/color/<int:pk>/', ColorAPIDetail.as_view()),

    path('hometask/car/', CarAPIview.as_view()),
    path('hometask/car/<int:pk>/', CarAPIDetail.as_view()),


]
