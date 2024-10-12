# Delivery Management System

A full-stack web application for managing vehicle service operations, including component registration, vehicle repair tracking, issue management, and revenue tracking with responsive graphs.

## Features
- Register components with repair or new purchase pricing.
- Add repair vehicles and manage related issues.
- Calculate final prices for repairs.
- Track daily, monthly, and yearly revenue using graphs.

## Tech Stack
- **Backend**: Django, Django REST Framework
- **Frontend**: React.js, Recharts
- **Database**: SQLite (Django default)
- **Testing**: Django’s built-in test framework

## Installation

### Backend Setup (Django)
1. Clone the repository and navigate to the backend folder:

   ```bash
   git clone https://github.com/saisandeepd7/Delivery-Management-System.git
   cd backend
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver

2. Frontend
  
   ```bash
   cd frontend
   npm install
   npm start

## API Endpoints

1. GET/POST /api/components/: Manage components.
2. GET/POST /api/vehicles/: Manage vehicles.
3. GET/POST /api/issues/: Manage vehicle issues.
4. GET /api/final_price/<vehicle_id>/: Calculate total price for vehicle repairs.
5. GET /api/revenue/<period>/: Fetch revenue data (daily, monthly, yearly).

## Running the Application

1. Ensure both the backend and frontend servers are running.
2. Access the frontend at http://localhost:3000 and the backend API at http://localhost:8000.