"""
URL configuration for crud_operation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from crud_operation import views
from department.views import department_page, save_department, delete_department

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage, name="home"),
    path('employees', views.indexPage, name="employees"),
    path('departments/', department_page, name="departments"),
    path('departments/add/', save_department, name="department_add"),
    path('departments/<int:pk>/edit/', save_department, name="department_edit"),
    path('departments/<int:pk>/delete/', delete_department, name="department_delete"),
]
