"""Forms for the students app.

This module exposes a `StudentForm` ModelForm. The `enrollment_date`
field accepts two common date formats to make data entry more
forgiving for users (dd/mm/YYYY and ISO YYYY-mm-dd).
"""

from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    enrollment_date = forms.DateField(
        input_formats=["%d/%m/%Y", "%Y-%m-%d"],
        required=False,
        error_messages={
            "invalid": "Enter a valid date. For example: 31/12/2024 or 2024-12-31"
        },
    )

    class Meta:
        model = Student
        fields = ["first_name", "last_name", "email", "matric_no", "enrollment_date"]
