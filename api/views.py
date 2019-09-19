from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializer import (
    ProvinceSerializer, Province,
    DistrictSerializer, District,
    CitySerializers, City
)


# provinces list
class ProvinceList(ListAPIView):

    queryset = Province.objects.values('sinhalaName',
                                       'englishName', 'featureImage', 'pk', 'mapUrl')
    serializer_class = ProvinceSerializer


# province detailview
class ProvinceDetail(RetrieveAPIView):

    model = Province
    serializer_class = ProvinceSerializer
    lookup_field = "id"

    def get_queryset(self):

        queryset = Province.objects.filter(pk=self.kwargs.get('id'))
        return queryset


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
