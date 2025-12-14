"""Views for student management and user signup.

This module contains a small signup helper and a set of class-based
views that operate on `Student` objects. All `Student` views are
protected with `LoginRequiredMixin` so users can only access their own
student records.
"""

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Student
from .forms import StudentForm


def signup_view(request):
    """Handle new user registration.

    Uses Django's `UserCreationForm`. On successful signup the user is
    logged in and redirected to the student list.
    """

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("student_list")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})


class StudentListView(LoginRequiredMixin, generic.ListView):
    """List students belonging to the authenticated user.

    - `LoginRequiredMixin` ensures anonymous users are redirected to
      the login page.
    - `get_queryset` restricts records to those owned by `request.user`.
    """

    model = Student
    template_name = "students/student_list.html"
    context_object_name = "students"
    login_url = "login"

    def get_queryset(self):
        return Student.objects.filter(user=self.request.user)


class StudentDetailView(LoginRequiredMixin, generic.DetailView):
    """Show a single student record, limited to the owner's records."""

    model = Student
    template_name = "students/student_detail.html"
    login_url = "login"

    def get_queryset(self):
        return Student.objects.filter(user=self.request.user)


class StudentCreateView(LoginRequiredMixin, generic.CreateView):
    """Create a new student and associate it with the logged-in user."""

    model = Student
    form_class = StudentForm
    template_name = "students/student_form.html"
    success_url = reverse_lazy("student_list")
    login_url = "login"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class StudentUpdateView(LoginRequiredMixin, generic.UpdateView):
    """Edit an existing student; user may only edit their own records."""

    model = Student
    form_class = StudentForm
    template_name = "students/student_form.html"
    success_url = reverse_lazy("student_list")
    login_url = "login"

    def get_queryset(self):
        return Student.objects.filter(user=self.request.user)


class StudentDeleteView(LoginRequiredMixin, generic.DeleteView):
    """Delete a student record owned by the authenticated user."""

    model = Student
    template_name = "students/student_confirm_delete.html"
    success_url = reverse_lazy("student_list")
    login_url = "login"

    def get_queryset(self):
        return Student.objects.filter(user=self.request.user)
