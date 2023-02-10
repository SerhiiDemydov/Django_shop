from django.test import TestCase
from django.urls import reverse

# Create your tests here.


class TestProductView(TestCase):

    def test_product_view(self):
        response = self.client.get(path=reverse("product"))
        # assert request.status_code == 200
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode("utf-8"), "Super good")
