from django.shortcuts import render
from .models import Employee, Role

# Create your views here.


def all_employees(request):
    """ A view for all employees page """
    employees = Employee.objects.all()

    context = {
        'employees': employees,
    }

    return render(request, 'employees/employees.html', context)
