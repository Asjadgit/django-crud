from django import forms
from department.models import Department
from .models import Employee


INPUT_CLASSES = (
    'w-full rounded-lg border border-gray-300 '
    'px-4 py-3 text-gray-900 '
    'placeholder-gray-400 shadow-sm '
    'focus:border-indigo-500 focus:outline-none '
    'focus:ring-2 focus:ring-indigo-200'
)


class EmployeeForm(forms.ModelForm):

    employee_depart = forms.ModelChoiceField(
        queryset=Department.objects.order_by('department_name'),
        empty_label='Select a department',
        label='Department',
        widget=forms.Select(attrs={'class': INPUT_CLASSES}),
    )

    class Meta:
        model = Employee
        fields = [
            'employee_name',
            'employee_age',
            'employee_email',
            'employee_phone',
            'employee_depart',
        ]
        labels = {
            'employee_name': 'Employee Name',
            'employee_age': 'Age',
            'employee_email': 'Email',
            'employee_phone': 'Phone',
        }
        widgets = {
            'employee_name': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'e.g. Ali Khan',
            }),
            'employee_age': forms.NumberInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'e.g. 28',
                'min': 18,
                'max': 100,
            }),
            'employee_email': forms.EmailInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'e.g. ali@example.com',
            }),
            'employee_phone': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'e.g. +92 300 1234567',
            }),
        }

    def clean_employee_age(self):
        age = self.cleaned_data['employee_age']
        if age < 18 or age > 100:
            raise forms.ValidationError('Age must be between 18 and 100.')
        return age

    def clean_employee_phone(self):
        phone = self.cleaned_data['employee_phone'].strip()
        digits = phone.replace('+', '').replace(' ', '').replace('-', '')
        if not digits.isdigit() or len(digits) < 11:
            raise forms.ValidationError('Enter a valid phone number.')
        return phone
