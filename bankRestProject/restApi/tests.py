from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Bank
from .serializers import BankSerializer

# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_bank(name="", address=""):
        if name != "" and address != "":
            Bank.objects.create(name=name, address=address)

    def setUp(self):
        # add test data
        self.create_bank("like glue", "sean paul")
        self.create_bank("simple song", "konshens")
        self.create_bank("love is wicked", "brick and lace")
        self.create_bank("jam rock", "damien marley")


class GetAllBanksTest(BaseViewTest):

    def test_get_all_banks(self):
        """
        This test ensures that all songs added in the setUp method
        exist when we make a GET request to the songs/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("bank-all")
        )
        # fetch the data from db
        expected = Bank.objects.all()
        serialized = BankSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)