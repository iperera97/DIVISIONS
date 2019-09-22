from Province.models import Province
from django.test import TestCase, TransactionTestCase


class TestProvince(TestCase):

    @classmethod
    def setUpTestData(cls):

        provinceData = {
            'introduction': "hello world to western province",
            "sinhalaName": "බස්නාහිර",
            "tamilName": "மேல்",
            "englishName": "Western Province",
        }

        cls.ProvinceOBJ = Province.objects.create(**provinceData)

    def test_names(self):

        self.assertEqual(self.ProvinceOBJ.sinhalaName, "බස්නාහිර")
        self.assertEqual(self.ProvinceOBJ.englishName, "Western Province")
        self.assertEqual(self.ProvinceOBJ.tamilName, "மேல்")

    def test_absoluteURL(self):

        EDIT_ENDPOINT = self.ProvinceOBJ.get_absolute_url()
        PROVINCE_ID = self.ProvinceOBJ.pk
        self.assertURLEqual(
            EDIT_ENDPOINT, "/adminpanel/provinces/edit/{}/".format(PROVINCE_ID)
        )
