from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class TestEmployeeList(TestCase):
    def test_empl_page_load(self):
        response = self.client.get("/employees")

        self.assertEqual(response.status_code, 200)