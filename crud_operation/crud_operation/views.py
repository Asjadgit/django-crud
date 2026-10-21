from django.http import HttpResponse
from django.shortcuts import render
from employee.models import Employee
from department.models import Department
from department.forms import DepartmentForm


def homePage(request):
    # return HttpResponse("Welcome to Employee Management Service!")
    return render(request, "home.html")

def indexPage(request):

    employees = Employee.objects.select_related("employee_depart").order_by("employee_name")

    return render(request, "employees/index.html", {
        "employees": employees,
        "department_count": Department.objects.count(),
    })

def departmentPage(request):
    departments = Department.objects.all()

    return render(
        request,
        'department/index.html',
        {'departments': departments}
    )

def adddepartmentPage(request):

    form = DepartmentForm()

    return render(
        request,
        'department/index.html',
        {'form': form}
    )