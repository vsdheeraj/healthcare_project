from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    
    class Meta:
        model = Patient
        fields = ['id', 'user', 'first_name', 'last_name', 'date_of_birth', 'gender', 
                  'blood_group', 'phone_number', 'email', 'address', 'medical_history', 
                  'allergies', 'emergency_contact_name', 'emergency_contact_phone', 
                  'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at'] 