from django.test import TestCase
from district.models import District
from Province.models import Province


class TestModel(TestCase):

    @classmethod
    def setUpTestData(cls):

        province_data = {
            'sinhalaName': "බස්නාහිර",
            "englishName": "Western",
            "tamilName": "மேல் மாகாணம்"
        }

        cls.province = Province.objects.create(**province_data)
        cls.district = District.objects.create(
            **province_data, province=cls.province
        )

    def test_absolute_url(self):

        ACTUAL_PATH = self.district.get_absolute_url()
        EXPECTED_URL = "/adminpanel/district/edit/{}/".format(
            self.district.pk)

        self.assertEqual(ACTUAL_PATH, EXPECTED_URL)

    def test_info(self):

        self.assertEqual(self.district.sinhalaName, "බස්නාහිර")
        self.assertEqual(self.district.englishName, "Western")
        self.assertEqual(self.district.tamilName, "மேல் மாகாணம்")
