from django.test import TestCase
from django.urls import reverse

from department.models import Department
from .forms import EmployeeForm


# Create your tests here.
class TestEmployeeList(TestCase):
    def test_empl_page_load(self):
        response = self.client.get(reverse("employees"))

        self.assertEqual(response.status_code, 200)


class EmployeeCreatePageTest(TestCase):

    def test_page_loads(self):
        response = self.client.get(reverse("employees_create"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Add Employee")

    def test_page_has_form(self):
        response = self.client.get(reverse("employees_create"))

        self.assertIsInstance(response.context["form"], EmployeeForm)

    def test_page_shows_departments(self):
        Department.objects.create(department_name="Finance")

        response = self.client.get(reverse("employees_create"))

        self.assertContains(response, "Finance")
