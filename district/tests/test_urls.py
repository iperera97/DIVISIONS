from django.test import TestCase
from django.shortcuts import reverse
from django.urls import resolve
from district import views


# test provinces endpoints
class TestUrls(TestCase):

    DISTRICT_ENDPOINT = "/adminpanel/district/"
    HOME_URL = "district:home"
    EDIT_URL = "district:edit"
    CREATE_URL = "district:create"
    REMOVE_URL = "district:delete"

    def test_home(self):

        # test endpoint
        url = reverse(self.HOME_URL)
        self.assertURLEqual(url, self.DISTRICT_ENDPOINT)

        # test function
        self.assertEqual(resolve(url).func.view_class, views.ViewDistrct)

    def test_edit(self):

        # test endpoint
        url = reverse(self.EDIT_URL, kwargs={"pk": 1})
        expected_endpoint = "{}{}".format(self.DISTRICT_ENDPOINT, 'edit/1/')
        self.assertURLEqual(url, expected_endpoint)

        # test function
        self.assertEqual(resolve(url).func.view_class, views.EditDistrict)

    def test_create(self):

        # test endpoint
        url = reverse(self.CREATE_URL)
        self.assertURLEqual(url, self.DISTRICT_ENDPOINT + "create/")

        # test function
        self.assertEqual(resolve(url).func.view_class, views.CreateDistrict)

    def test_remove(self):

            # test endpoint
        url = reverse(self.REMOVE_URL, kwargs={"pk": 1})
        self.assertEqual(url, self.DISTRICT_ENDPOINT + "remove/1/")

        # test function
        self.assertEqual(resolve(url).func.view_class, views.RemoveDistrict)
