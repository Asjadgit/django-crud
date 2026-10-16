from django.db import models
from department.models import Department

# Create your models here.
class Employee(models.Model):
    employee_name   = models.CharField(max_length=100)
    employee_age    = models.BigIntegerField()
    employee_email  = models.EmailField(max_length=254)
    employee_phone  = models.CharField(max_length=20)
    employee_depart = models.ForeignKey(Department, on_delete=models.PROTECT)

