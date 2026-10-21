
from django import forms
from .models import Department


class DepartmentForm(forms.ModelForm):

    class Meta:
        model = Department
        fields = ['department_name']
        labels = {
            'department_name': 'Department Name',
        }
        widgets = {
            'department_name': forms.TextInput(attrs={
                'class': (
                    'w-full rounded-lg border border-gray-300 '
                    'px-4 py-3 text-gray-900 '
                    'placeholder-gray-400 shadow-sm '
                    'focus:border-indigo-500 focus:outline-none '
                    'focus:ring-2 focus:ring-indigo-200'
                ),
                'placeholder': 'e.g. Human Resources',
            }),
        }
