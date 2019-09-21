from rest_framework import serializers
from Province.models import Province
from district.models import District
from city.models import City


class ProvinceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Province
        fields = ('pk',
                  'introduction',
                  'sinhalaName',
                  'englishName',
                  'tamilName',
                  'area',
                  'featureImage',
                  'mapUrl')

    featureImage = serializers.CharField(max_length=255, allow_blank=True)


class DistrictSerializer(serializers.ModelSerializer):

    class Meta:
        model = District
        fields = ('pk',
                  'introduction',
                  'province',
                  'sinhalaName',
                  'englishName',
                  'tamilName',
                  'area',
                  'featureImage',
                  'mapUrl')

    featureImage = serializers.CharField(max_length=255, allow_blank=True)
    province = serializers.PrimaryKeyRelatedField(read_only=True)


class CitySerializers(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ('pk',
                  'introduction',
                  'sinhalaName',
                  'englishName',
                  'tamilName',
                  'area',
                  'featureImage',
                  'mapUrl',
                  'district')
