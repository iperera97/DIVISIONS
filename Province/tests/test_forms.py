from django.test import SimpleTestCase, TestCase
from Province.forms import ProvinceForm
from Province.models import Province



class TestProvinceForm(TestCase):

    REQUIRED_FIELDS = {
        'introduction': "hello world to western province",
        "sinhalaName": "බස්නාහිර",
        "tamilName": "மேல்",
        "englishName": "Western Province",
    }

    @classmethod
    def setUpTestData(cls):
        pass

    def test_is_valid_form(self):

        FORM = ProvinceForm(self.REQUIRED_FIELDS)
        self.assertTrue(FORM.is_valid())

    def add_exist_province(self):

        FORM_2 = ProvinceForm(self.REQUIRED_FIELDS)
        FORM_2.save()

    def test_exist_name(self):

        FORM_1 = ProvinceForm(self.REQUIRED_FIELDS)

        # first one
        if FORM_1.is_valid():

            ProvinceForm(self.REQUIRED_FIELDS)
            FORM_1.save()

        # sinhala,  english , tamil names are unique
        self.assertRaises(Exception, self.add_exist_province)
