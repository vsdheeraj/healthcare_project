from rest_framework import serializers
from .models import PatientDoctorMapping
from patients.serializers import PatientSerializer
from doctors.serializers import DoctorSerializer
from patients.models import Patient
from doctors.models import Doctor

class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    patient_details = PatientSerializer(source='patient', read_only=True)
    doctor_details = DoctorSerializer(source='doctor', read_only=True)
    
    class Meta:
        model = PatientDoctorMapping
        fields = ['id', 'patient', 'doctor', 'patient_details', 'doctor_details', 
                  'assigned_date', 'notes', 'created_at', 'updated_at']
        read_only_fields = ['id', 'assigned_date', 'created_at', 'updated_at']
    
    def validate(self, attrs):
        # Validate that the patient belongs to the current user
        patient = attrs.get('patient')
        request = self.context.get('request')
        
        if patient and request and patient.user != request.user:
            raise serializers.ValidationError({"patient": "You can only map your own patients."})
        
        return attrs 