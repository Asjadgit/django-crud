from django.shortcuts import render
from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_POST

# Create your views here.
from .models import Department
from .forms import DepartmentForm

def department_page(request):
    return render(request, "department/index.html",{
        "form": DepartmentForm(),
        "departments": Department.objects.order_by("department_name")
    })

@require_POST
def save_department(request, pk=None):
    department = get_object_or_404(Department, pk=pk) if pk else None
    form       = DepartmentForm(request.POST, instance=department)

    if form.is_valid():
        form.save()
        messages.success(request, "Department Updated." if department else "Department Added.")
        return JsonResponse({"ok": True})

    return JsonResponse({"ok": False, "errors": form.errors}, status=400)

@require_POST
def delete_department(request, pk):
    department = get_object_or_404(Department, pk=pk)
    department.delete();
    messages.success(request, "Department Deleted.")
    return JsonResponse({"ok": True})
