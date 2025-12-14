# Django Project Startup Script
# This script sets up and runs the Django development server

Write-Host "Starting Django project setup..." -ForegroundColor Green

# Step 1: Create virtual environment if it doesn't exist
if (-Not (Test-Path ".\.venv")) {
    Write-Host "Creating virtual environment..." -ForegroundColor Yellow
    python -m venv .venv
}

# Step 2: Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
.\.venv\Scripts\Activate.ps1

# Step 3: Run migrations
Write-Host "Running migrations..." -ForegroundColor Yellow
python manage.py migrate

# Step 4: Start the development server
Write-Host "Starting Django development server..." -ForegroundColor Green
Write-Host "Open your browser to http://127.0.0.1:8000/" -ForegroundColor Cyan
python manage.py runserver
