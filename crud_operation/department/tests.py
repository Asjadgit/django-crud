from django.test import TestCase
from django.urls import reverse

from .models import Department



class DepartmentPageTest(TestCase):

    def test_page_loads(self):
        response = self.client.get(reverse("departments"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Add Department")

    def test_page_lists_departments(self):
        Department.objects.create(department_name="Finance")

        response = self.client.get(reverse("departments"))

        self.assertContains(response, "Finance")
