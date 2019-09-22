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


# province serialzer by district
class RelatedProvinceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Province
        fields = ('pk',
                  'englishName',)


class DistrictSerializer(serializers.ModelSerializer):

    province = RelatedProvinceSerializer()
    featureImage = serializers.CharField(max_length=255, allow_blank=True)

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
