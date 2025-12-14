from django.contrib import admin
from django.urls import path, include
from students.views import signup_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("students.urls")),
]
