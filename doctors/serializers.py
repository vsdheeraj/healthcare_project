from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    
    class Meta:
        model = Doctor
        fields = ['id', 'user', 'first_name', 'last_name', 'gender', 'specialization', 
                  'license_number', 'phone_number', 'email', 'address', 
                  'years_of_experience', 'bio', 'availability', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at'] 