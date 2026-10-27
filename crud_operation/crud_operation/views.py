from django.http import HttpResponse
from django.shortcuts import render
from employee.models import Employee
from department.models import Department
from department.forms import DepartmentForm


def homePage(request):
    # return HttpResponse("Welcome to Employee Management Service!")
    return render(request, "home.html")