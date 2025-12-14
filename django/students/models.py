"""Student model.

This module defines the `Student` model used by the app. Each Student
record is associated with a Django `User` (the owner) so that the
application can restrict access to each user's students.

Fields:
 - `user`: the Django `User` who created/owns this student record.
 - `first_name`, `last_name`: human-readable name fields.
 - `email`: contact email for the student.
 - `matric_no`: an identifier (e.g. matriculation number) used by the
     university or organisation.
 - `enrollment_date`: optional date when the student enrolled.
"""

from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    """Represent a student belonging to a particular `User`.

    The `related_name="students"` on the ForeignKey makes it easy to
    access all students for a user via `some_user.students.all()`.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="students")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    matric_no = models.CharField(max_length=30)
    enrollment_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.matric_no})"
