Little Lemon Back-End Capstone Project

Built with Django, Django REST Framework, MySQL, and Djoser.

SETUP
1. Create and activate a Python virtual environment.
2. Enter the littlelemon folder containing manage.py.
3. Install dependencies:
   python -m pip install -r requirements.txt
4. Create a MySQL database named littlelemon.
5. Update the database USER in littlelemon/settings.py if needed.
6. Set the MYSQL_PASSWORD environment variable to your MySQL password.

PowerShell:
   $credential = Read-Host "MySQL password" -AsSecureString
   $env:MYSQL_PASSWORD = [System.Net.NetworkCredential]::new('', $credential).Password

7. Run:
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver

BASE URL
http://127.0.0.1:8000

HOME PAGE
GET /restaurant/

MENU API
GET, POST /restaurant/menu/items/
GET, PUT, PATCH, DELETE /restaurant/menu/items/<id>/

Example menu POST body:
{
  "Title": "Greek Salad",
  "Price": "12.99",
  "Inventory": 20
}

BOOKING API - TOKEN REQUIRED
GET, POST /restaurant/booking/tables/
GET, PUT, PATCH, DELETE /restaurant/booking/tables/<id>/

Example booking POST body:
{
  "Name": "Test Customer",
  "No_of_guests": 4,
  "BookingDate": "2026-12-15T18:00:00Z"
}

USER REGISTRATION
POST /auth/users/
Body: username, email, password

TOKEN LOGIN
POST /auth/token/login/
Body: username, password
Response contains auth_token.

ALTERNATIVE TOKEN ENDPOINT
POST /restaurant/api-token-auth/
Body: username, password
Response contains token.

AUTHENTICATED REQUESTS
Add this HTTP header in Insomnia:
Authorization: Token YOUR_TOKEN

TOKEN LOGOUT
POST /auth/token/logout/
Include the Authorization header.

ADMIN
/admin/
Create your own superuser using the setup command above.

TESTS
From the folder containing manage.py:
python manage.py test tests

Tests cover the Menu model string representation and
the menu list API response.