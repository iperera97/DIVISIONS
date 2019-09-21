from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
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


# get releventDistrict
class ReleventDistrict(APIView):

    def get(self, request, *args, **kwargs):

        queryset = District.objects.filter(
            province_id=kwargs.get('province_id'))
        queryset = queryset.values(
            'englishName', 'pk')

        if queryset:
            status = 200
        else:
            status = 404

        return Response(queryset, status=status)


class GetDistrict(ListAPIView):

    serializer_class = DistrictSerializer

    def get_queryset(self):

        queryset = District.objects.all()
        return queryset


class DistrictDetail(RetrieveAPIView):

    model = District
    serializer_class = DistrictSerializer
    lookup_field = "id"

    def get_queryset(self):

        queryset = District.objects.filter(pk=self.kwargs.get('id'))
        return queryset


class FindDistrict(APIView):

    def get(self, request, *args, **kwargs):
        searchValue = request.GET.get('englishName')
        queryset = District.objects.filter(
            englishName__istartswith=searchValue)

        queryset = queryset.values('englishName', 'pk')
        return Response(queryset)


class GetCity(ListAPIView):

    serializer_class = CitySerializers

    def get_queryset(self, request, *args, **kwargs):

        queryset = City.objects.all()
        queryset = queryset.select_related('district')
        return queryset
