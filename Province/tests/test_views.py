from django.test import TestCase, Client
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from Province.models import Province


class TestProvinceView(TestCase):

    @classmethod
    def setUpTestData(cls):

        # used templates
        cls.TEMPLATES = {
            'list': 'Province/province_list.html',
            'create': 'Province/create_province.html',
            'edit': 'Province/edit_province.html',
        }

        # urls
        cls.ENDPOINTS = {
            'list': "provinces:home",
            'create': "provinces:create",
            'edit': "provinces:edit",
            'remove': "provinces:remove",
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

        # create province
        self.obj = Province.objects.create(
            sinhalaName="බස්නාහිර",
            englishName="Western Province",
            tamilName="மேல்"
        )

    def test_view_province(self):

        viewProvinceURL = reverse(self.ENDPOINTS.get("list"))
        response = self.client.get(viewProvinceURL)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "Province/province_list.html")
        self.assertEqual(response.context.get("title"), "Province")

    def test_create_province(self):

        URL = reverse(self.ENDPOINTS.get("create"))
        getResponse = self.client.get(URL)

        # get
        self.assertEqual(getResponse.status_code, 200)
        self.assertTemplateUsed(getResponse, "Province/create_province.html")

    def test_edit_province(self):

        URL = reverse(self.ENDPOINTS.get("edit"), kwargs={'pk': self.obj.pk})
        getResponse = self.client.get(URL)

        # get
        self.assertEqual(getResponse.status_code, 200)
        self.assertTemplateUsed(getResponse, "Province/edit_province.html")

    def test_remove_province(self):

        URL = reverse(self.ENDPOINTS.get("remove"), kwargs={'pk': self.obj.pk})
        getResponse = self.client.get(URL)

        # get
        self.assertEqual(getResponse.status_code, 302)
