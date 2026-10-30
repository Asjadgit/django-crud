from django.shortcuts import render
from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect

# Create your views here.
from .models import Employee
from .forms import EmployeeForm
from department.models import Department

def indexPage(request):

    employees = Employee.objects.select_related("employee_depart").order_by("employee_name")

    return render(request, "employees/index.html", {
        "employees": employees,
        "department_count": Department.objects.count(),
    })

def createPage(request):
    return render(request, "employees/create.html", {"form" : EmployeeForm()})


@require_POST
def storeEmployee(request):
    form = EmployeeForm(request.POST)

    if form.is_valid():
        form.save();
        messages.success(request, "Employee Added Successfully!")
        return redirect("employees")

    return render(request, "employees/create.html", {"form": form}, status=400)