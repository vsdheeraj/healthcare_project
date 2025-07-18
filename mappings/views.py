from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import PatientDoctorMapping
from .serializers import PatientDoctorMappingSerializer
from patients.models import Patient

class IsPatientOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow only if the user owns the patient in the mapping
        return obj.patient.user == request.user

class PatientDoctorMappingViewSet(viewsets.ModelViewSet):
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated, IsPatientOwner]
    
    def get_queryset(self):
        # Get all mappings where the patient belongs to the current user
        return PatientDoctorMapping.objects.filter(patient__user=self.request.user)
    
    @action(detail=False, methods=['get'], url_path='patient/(?P<patient_id>[^/.]+)')
    def patient_mappings(self, request, patient_id=None):
        """
        Get all doctors assigned to a specific patient
        """
        try:
            patient = Patient.objects.get(id=patient_id, user=request.user)
        except Patient.DoesNotExist:
            return Response(
                {"detail": "Patient not found or you don't have permission to view this patient."},
                status=status.HTTP_404_NOT_FOUND
            )
        
        mappings = PatientDoctorMapping.objects.filter(patient=patient)
        serializer = self.get_serializer(mappings, many=True)
        return Response(serializer.data)
