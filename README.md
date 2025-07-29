
Flask API Test
==============

A simple Python Flask-based REST API that demonstrates how to create basic GET and POST endpoints. Ideal for beginners exploring API development.

Features:
---------
- GET / – Welcome route
- GET /greet?name=YourName – Returns a personalized greeting
- POST /add – Accepts two numbers in JSON and returns their sum

Project Structure:
------------------
flask-api-test/
├── app.py         # Main Flask API code
└── README.txt     # This file

Getting Started:
----------------
1. Clone the Repository:
   git clone https://github.com/Amogh-Kapse/flask-api-test.git
   cd flask-api-test

2. (Optional) Create Virtual Environment:
   python -m venv venv
   venv\Scripts\activate  (On Windows)

3. Install Flask:
   pip install Flask

4. Run the Application:
   python app.py

   It will start on:
   http://127.0.0.1:5000/

API Endpoints:
--------------
1. GET /
   - Returns a welcome message.
   - Example: http://127.0.0.1:5000/
   - Response: Welcome to my API!

2. GET /greet
   - Returns a personalized greeting.
   - Example: http://127.0.0.1:5000/greet?name=Amogh
   - Response: { "message": "Hello, Amogh!" }

3. POST /add
   - Accepts two numbers and returns their sum.
   - POST to: http://127.0.0.1:5000/add
   - JSON Body: { "a": 5, "b": 7 }
   - Response: { "result": 12 }

Testing Tools:
--------------
- Browser (for GET)
- Postman or Insomnia (for POST)
- curl in terminal:

  curl -X POST http://127.0.0.1:5000/add -H "Content-Type: application/json" -d "{\"a\":10, \"b\":20}"

Requirements:
-------------
- Python 3.7+
- Flask (pip install Flask)

Future Improvements:
--------------------
- Add input validation
- Add subtraction/multiplication endpoints
- Add authentication (API Key, JWT)
- Connect to a database (SQLite, PostgreSQL)
- Deploy on Render/Heroku

Author:
-------
Made by Amogh Kapse (https://github.com/Amogh-Kapse)
