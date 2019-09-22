from django.test import TestCase, Client
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from district.forms import DistrictInitForm
from Province.models import Province
from district.models import District


class DistrictView(TestCase):

    @classmethod
    def setUpTestData(cls):

        cls.ENDPOINTS = {
            'list': reverse('district:home'),
            'create': reverse('district:create'),
        }

        cls.TITLES = {
            'list': 'Districts',
            'create': 'Create District'
        }

        cls.FORM_DATA = {
            "introduction": "test content goes here",
            'sinhalaName': "බස්නාහිර",
            "englishName": "Western",
            "tamilName": "மேல் மாகாணம்",
        }

    def setUp(self):

        # create test user
        USERNAME = "root"
        PASSWORD = "public_place123"
        EMAIL = "root@gmail.com"

        User = get_user_model()
        User.objects.create_superuser(
            username=USERNAME, password=PASSWORD, email=EMAIL)

        # init client
        self.client = Client()
        self.client.login(username=USERNAME, password=PASSWORD)

    def test_list(self):

        response = self.client.get(self.ENDPOINTS.get("list"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'district/home.html')
        self.assertEqual(response.context.get(
            "title"), self.TITLES.get('list'))

    def test_create(self):

        response = self.client.get(self.ENDPOINTS.get("create"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'district/create.html')
        self.assertEqual(response.context.get(
            "title"), self.TITLES.get('create'))

    def test_create_form(self):

        self.FORM_DATA = {**self.FORM_DATA,
                          'province': Province.objects.create(**self.FORM_DATA).pk
                          }

        form1 = DistrictInitForm(data=self.FORM_DATA)

        self.assertTrue(form1.is_valid())
        self.assertIsInstance(form1.save(), District)
