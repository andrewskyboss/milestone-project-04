from django.shortcuts import render, get_object_or_404
from .models import Employee, Role

# Create your views here.


def all_employees(request):
    """ A view for all employees page """
    employees = Employee.objects.all()

    context = {
        'employees': employees,
    }

    return render(request, 'employees/employees.html', context)


def employee_detail(request, employee_id):
    """ A view to show individual employee details """

    employee = get_object_or_404(Employee, pk=employee_id)

    context = {
        'employee': employee,
    }

    return render(request, 'employees/employee_detail.html', context)
