#!/bin/bash
echo "Creating virtual environment..."
python3 -m venv venv
echo "Activating virtual environment..."
source venv/bin/activate
echo "Installing dependencies..."
pip install -r requirements.txt
echo "Creating database tables..."
python manage.py makemigrations
python manage.py migrate
echo "Creating test data..."
python manage.py create_test_data
echo "Starting server..."
python manage.py runserver 