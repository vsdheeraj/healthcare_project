"""
URL configuration for healthcare_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from django.http import JsonResponse

def health_check(request):
    return JsonResponse({"status": "ok"})

def models_endpoint(request):
    return JsonResponse({
        "data": [],
        "object": "list"
    })

def root_view(request):
    # Handle the root URL
    return JsonResponse({
        "message": "Welcome to the Healthcare API",
        "version": "1.0.0",
        "endpoints": {
            "authentication": "/api/auth/",
            "patients": "/api/patients/",
            "doctors": "/api/doctors/",
            "mappings": "/api/mappings/",
            "health_check": "/health/",
            "admin": "/admin/"
        }
    })

urlpatterns = [
    path("admin/", admin.site.urls),
    path("health/", health_check, name="health_check"),
    path("api/auth/", include("authentication.urls")),
    path("api/patients/", include("patients.urls")),
    path("api/doctors/", include("doctors.urls")),
    path("api/mappings/", include("mappings.urls")),
    path("v1/models", models_endpoint, name="models_endpoint"),
    path("", root_view, name="root"),
]
