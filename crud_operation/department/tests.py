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

    def test_add_rejects_get(self):
        response = self.client.get(reverse("department_add"))

        self.assertEqual(response.status_code, 405)
    
    def test_add_creates_department(self):
        response = self.client.post(reverse("department_add"), {"department_name": "Finance"})

        self.assertEqual(Department.objects.count(), 1)
    
    def test_add_empty_name_fails(self):
        response = self.client.post(reverse("department_add"), {"department_name": ""})

        self.assertEqual(response.status_code, 400)
        self.assertEqual(Department.objects.count(), 0)

    def test_add_returns_ok_json(self):
        response = self.client.post(reverse("department_add"), {"department_name": "Finance"})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"ok": True})

class DeartmentEditPageTest(TestCase):
    def test_edit_Updates_department(self):
        department = Department.objects.create(department_name="Finance")

        url = reverse("department_edit", args=[department.pk])
        response = self.client.post(url, {"department_name": "Accounts"})

        self.assertEqual(response.status_code, 200)
        department.refresh_from_db()
        self.assertEqual(department.department_name, "Accounts")


class DeartmentDeletePageTest(TestCase):
    def test_delete_department(self):
        department = Department.objects.create(department_name="Finance")

        url = reverse("department_delete", args=[department.pk])
        response = self.client.post(url,)

        self.assertEqual(response.status_code, 200)
    
        self.assertFalse(Department.objects.filter(pk=department.pk).exists())