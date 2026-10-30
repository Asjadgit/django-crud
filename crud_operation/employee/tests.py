from django.test import TestCase
from django.urls import reverse

from department.models import Department
from .forms import EmployeeForm
from .models import Employee


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


class EmployeeStorePageTest(TestCase):

    def setUp(self):
        self.department = Department.objects.create(department_name="Finance")
        self.url = reverse("employees_store")

    def valid_data(self, **overrides):
        data = {
            "employee_name": "Ali Khan",
            "employee_age": 28,
            "employee_email": "ali@example.com",
            "employee_phone": "03001234567",
            "employee_depart": self.department.pk,
        }
        data.update(overrides)
        return data

    def test_store_rejects_get(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 405)

    def test_store_creates_employee(self):
        self.client.post(self.url, self.valid_data())

        self.assertEqual(Employee.objects.count(), 1)
        employee = Employee.objects.get()
        self.assertEqual(employee.employee_name, "Ali Khan")
        self.assertEqual(employee.employee_depart, self.department)

    def test_store_redirects_to_list(self):
        response = self.client.post(self.url, self.valid_data())

        self.assertRedirects(response, reverse("employees"))

    def test_store_empty_form_fails(self):
        response = self.client.post(self.url, {})

        self.assertEqual(response.status_code, 400)
        self.assertEqual(Employee.objects.count(), 0)

    def test_store_invalid_age_fails(self):
        response = self.client.post(self.url, self.valid_data(employee_age=10))

        self.assertEqual(response.status_code, 400)
        self.assertContains(response, "Age must be between 18 and 100.", status_code=400)
        self.assertEqual(Employee.objects.count(), 0)

    def test_store_invalid_email_fails(self):
        response = self.client.post(self.url, self.valid_data(employee_email="not-an-email"))

        self.assertEqual(response.status_code, 400)
        self.assertEqual(Employee.objects.count(), 0)

    def test_store_invalid_phone_fails(self):
        response = self.client.post(self.url, self.valid_data(employee_phone="12345"))

        self.assertEqual(response.status_code, 400)
        self.assertContains(response, "Enter a valid phone number.", status_code=400)
        self.assertEqual(Employee.objects.count(), 0)

    def test_store_unknown_department_fails(self):
        response = self.client.post(self.url, self.valid_data(employee_depart=999))

        self.assertEqual(response.status_code, 400)
        self.assertEqual(Employee.objects.count(), 0)

    def test_store_keeps_typed_values_on_error(self):
        response = self.client.post(self.url, self.valid_data(employee_age=10))

        self.assertContains(response, "Ali Khan", status_code=400)