from django.test import TestCase
from django.shortcuts import reverse
from django.urls import resolve
from Province import views


# test provinces endpoints
class TestUrls(TestCase):

    PROVINCE_ENDPOINT = "/adminpanel/provinces/"
    HOME_URL = "provinces:home"
    EDIT_URL = "provinces:edit"
    CREATE_URL = "provinces:create"
    REMOVE_URL = "provinces:remove"

    def test_home(self):

        # test endpoint
        url = reverse(self.HOME_URL)
        self.assertURLEqual(url, self.PROVINCE_ENDPOINT)

        # test function
        self.assertEqual(resolve(url).func.view_class, views.ViewProvinces)

    def test_edit(self):

        # test endpoint
        url = reverse(self.EDIT_URL, kwargs={"pk": 1})
        expected_endpoint = "{}{}".format(self.PROVINCE_ENDPOINT, 'edit/1/')
        self.assertURLEqual(url, expected_endpoint)

        # test function
        self.assertEqual(resolve(url).func.view_class, views.EditProvinces)

    def test_create(self):

        # test endpoint
        url = reverse(self.CREATE_URL)
        self.assertURLEqual(url, self.PROVINCE_ENDPOINT + "create/")

        # test function
        self.assertEqual(resolve(url).func.view_class, views.CreateProvince)

    def test_remove(self):

            # test endpoint
        url = reverse(self.REMOVE_URL, kwargs={"pk": 1})
        self.assertEqual(url, self.PROVINCE_ENDPOINT + "remove/1/")

        # test function
        self.assertEqual(resolve(url).func.view_class, views.RemoveProvince)
