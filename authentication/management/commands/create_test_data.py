from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from authentication.models import UserProfile
from patients.models import Patient
from doctors.models import Doctor
from mappings.models import PatientDoctorMapping
from datetime import date, timedelta
import random

class Command(BaseCommand):
    help = 'Create test data for the healthcare application'

    def handle(self, *args, **options):
        self.stdout.write('Creating test data...')
        
        # Create test users
        test_users = []
        for i in range(1, 4):
            username = f'testuser{i}'
            email = f'testuser{i}@example.com'
            
            # Check if user already exists
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password='password123',
                    first_name=f'Test{i}',
                    last_name=f'User{i}'
                )
                
                # Create user profile
                UserProfile.objects.create(
                    user=user,
                    phone_number=f'555-555-{1000+i}',
                    address=f'Test Address {i}, Test City'
                )
                
                test_users.append(user)
                self.stdout.write(self.style.SUCCESS(f'Created user: {username}'))
            else:
                test_users.append(User.objects.get(username=username))
                self.stdout.write(f'User {username} already exists')
        
        # Create test patients
        specializations = [choice[0] for choice in Doctor.SPECIALIZATION_CHOICES]
        blood_groups = [choice[0] for choice in Patient.BLOOD_GROUP_CHOICES]
        
        for user in test_users:
            # Create patients for each user
            for i in range(1, 4):
                patient_name = f'Patient{i}'
                
                # Check if patient already exists
                if not Patient.objects.filter(first_name=patient_name, user=user).exists():
                    patient = Patient.objects.create(
                        user=user,
                        first_name=patient_name,
                        last_name=f'Test{i}',
                        date_of_birth=date.today() - timedelta(days=365*random.randint(20, 80)),
                        gender=random.choice(['M', 'F']),
                        blood_group=random.choice(blood_groups),
                        phone_number=f'555-123-{1000+i}',
                        email=f'patient{i}_{user.id}@example.com',
                        address=f'Patient Address {i}, Patient City',
                        medical_history='No significant medical history',
                        allergies='None'
                    )
                    self.stdout.write(self.style.SUCCESS(f'Created patient: {patient}'))
                else:
                    self.stdout.write(f'Patient {patient_name} already exists for user {user.username}')
            
            # Create doctors for each user
            for i in range(1, 3):
                doctor_name = f'Doctor{i}'
                
                # Check if doctor already exists
                if not Doctor.objects.filter(first_name=doctor_name, user=user).exists():
                    doctor = Doctor.objects.create(
                        user=user,
                        first_name=doctor_name,
                        last_name=f'Test{i}',
                        gender=random.choice(['M', 'F']),
                        specialization=random.choice(specializations),
                        license_number=f'LIC{user.id}{i}{random.randint(1000, 9999)}',
                        phone_number=f'555-456-{1000+i}',
                        email=f'doctor{i}_{user.id}@example.com',
                        address=f'Doctor Address {i}, Doctor City',
                        years_of_experience=random.randint(1, 30),
                        bio=f'Experienced doctor with specialization in various fields.',
                        availability='Monday to Friday, 9 AM to 5 PM'
                    )
                    self.stdout.write(self.style.SUCCESS(f'Created doctor: {doctor}'))
                else:
                    self.stdout.write(f'Doctor {doctor_name} already exists for user {user.username}')
        
        # Create mappings
        patients = Patient.objects.all()
        doctors = Doctor.objects.all()
        
        for patient in patients:
            # Assign 1-2 doctors to each patient
            for i in range(random.randint(1, 2)):
                if i < len(doctors):
                    doctor = random.choice(doctors)
                    
                    # Check if mapping already exists
                    if not PatientDoctorMapping.objects.filter(patient=patient, doctor=doctor).exists():
                        mapping = PatientDoctorMapping.objects.create(
                            patient=patient,
                            doctor=doctor,
                            notes=f'Regular check-up for {patient}'
                        )
                        self.stdout.write(self.style.SUCCESS(f'Created mapping: {mapping}'))
                    else:
                        self.stdout.write(f'Mapping between {patient} and {doctor} already exists')
        
        self.stdout.write(self.style.SUCCESS('Test data creation completed!')) 