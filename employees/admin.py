from django.contrib import admin
from .models import Employee, Role

# Register your models here.


class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'role',
        'start_date',
        'description',
        'qualifications',
        'interests',
        'more',
        'image',
    )

    ordering = ('sku',)


class RoleAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


# Register your models here.

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Role, RoleAdmin)
