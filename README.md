# Healthcare Backend API

A robust Django REST Framework backend for healthcare management, enabling secure patient and doctor record management with JWT authentication.

## Features

- **User Authentication**: Secure JWT-based authentication system
- **Patient Management**: CRUD operations for patient records with ownership controls
- **Doctor Management**: Comprehensive doctor profile management
- **Patient-Doctor Mapping**: Associate doctors with patients for treatment tracking
- **RESTful API**: Well-structured endpoints following REST principles
- **PostgreSQL Database**: Reliable data storage with proper relationships
- **Security**: Permission-based access control and data validation

## Tech Stack

- Django 4.2.7
- Django REST Framework 3.14.0
- PostgreSQL
- JWT Authentication (djangorestframework-simplejwt)

## API Endpoints

### Authentication
- POST /api/auth/register/ - Register a new user
- POST /api/auth/login/ - Login and get JWT token
- GET /api/auth/me/ - Get user profile

### Patient Management
- POST /api/patients/ - Add a new patient
- GET /api/patients/ - Get all patients for the authenticated user
- GET /api/patients/<id>/ - Get patient details
- PUT /api/patients/<id>/ - Update patient
- DELETE /api/patients/<id>/ - Delete patient

### Doctor Management
- POST /api/doctors/ - Add a new doctor
- GET /api/doctors/ - Get all doctors
- GET /api/doctors/<id>/ - Get doctor details
- PUT /api/doctors/<id>/ - Update doctor
- DELETE /api/doctors/<id>/ - Delete doctor

### Patient-Doctor Mapping
- POST /api/mappings/ - Assign doctor to patient
- GET /api/mappings/ - Get all mappings for the authenticated user's patients
- GET /api/mappings/patient/<patient_id>/ - Get doctors for a specific patient
- DELETE /api/mappings/<id>/ - Remove doctor from patient

## Setup Instructions

1. Clone the repository
   ```
   git clone https://github.com/yourusername/healthcare-backend.git
   cd healthcare-backend
   ```

2. Create a virtual environment
   ```
   python -m venv venv
   ```

3. Activate the virtual environment
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`

4. Install dependencies
   ```
   pip install -r requirements.txt
   ```

5. Create a PostgreSQL database named `healthcare_db`

6. Create a `.env` file in the project root with the following content
   ```
   SECRET_KEY=your-secret-key
   DEBUG=True
   DB_NAME=healthcare_db
   DB_USER=postgres
   DB_PASSWORD=your-password
   DB_HOST=localhost
   DB_PORT=5433
   ```

7. Run migrations
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

8. Create test data (optional)
   ```
   python manage.py create_test_data
   ```

9. Start the development server
   ```
   python manage.py runserver
   ```

## Testing

A Postman collection is included in the repository for API testing.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 