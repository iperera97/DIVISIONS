from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .serializer import (
    ProvinceSerializer, Province,
    DistrictSerializer, District,
    CitySerializers, City
)


class GetProvinces(ListAPIView):

    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer


class GetDistrict(ListAPIView):

    serializer_class = DistrictSerializer

    def get_queryset(self):

        queryset = District.objects.all()
        queryset = queryset.select_related('province')
        return queryset


class GetCity(ListAPIView):

    serializer_class = CitySerializers

    def get_queryset(self):

        queryset = City.objects.all()
        queryset = queryset.select_related('district')
        return queryset
