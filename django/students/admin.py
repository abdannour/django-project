"""Admin registration for the Student model.

Registering `Student` with a small admin configuration so project
maintainers can view and search records in the admin interface.
"""

from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "matric_no", "email", "enrollment_date")
    search_fields = ("first_name", "last_name", "matric_no", "email")
