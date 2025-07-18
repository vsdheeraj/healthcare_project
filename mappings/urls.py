from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientDoctorMappingViewSet

router = DefaultRouter()
router.register(r'', PatientDoctorMappingViewSet, basename='mapping')

urlpatterns = [
    path('', include(router.urls)),
] 