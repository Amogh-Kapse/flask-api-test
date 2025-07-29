
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

💡 What Can You Use This For?

This is a starting point for building real APIs. Here's how you can use or expand this:
✅ 1. Backend for a Web or Mobile App

    Your frontend (React, Android, etc.) can talk to this API.
    Example: A to-do list app where /add adds tasks, /delete deletes tasks.

✅ 2. Machine Learning/AI APIs

    Expose your ML model to the internet:

        Send image/text as input via POST.
        Return predictions as JSON.
    Example: /predict route that returns spam/ham for a message.

✅ 3. Internal Tools

    Automate reports, calculations, or status checks.
    Example: API for generating PDFs, summaries, etc.

✅ 4. Microservices

    As part of a larger distributed system.
    Each API can handle a specific feature (user auth, payments, etc.).

✅ 5. Automation & Integrations

    Connect your Python code to other tools (Zapier, Slack, etc.).
    Example: An API that receives a webhook and triggers a script.

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
