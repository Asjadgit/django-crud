
from django.test import TestCase


class DepartmentPageTest(TestCase):

    def test_dept_list_table(self):
        response = self.client.get("/departemnts")

        self.assertEqual(response.status_code, 200)
