"""URL patterns for the `students` app.

Each URL is named so templates and redirects can reference them by
name rather than hard-coding paths. Class-based views are used for
common CRUD operations.
"""

from django.urls import path, include
from . import views

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("signup/", views.signup_view, name="signup"),
    path("", views.StudentListView.as_view(), name="student_list"),
    path("student/add/", views.StudentCreateView.as_view(), name="student_add"),
    path("student/<int:pk>/", views.StudentDetailView.as_view(), name="student_detail"),
    path(
        "student/<int:pk>/edit/", views.StudentUpdateView.as_view(), name="student_edit"
    ),
    path(
        "student/<int:pk>/delete/",
        views.StudentDeleteView.as_view(),
        name="student_delete",
    ),
]
