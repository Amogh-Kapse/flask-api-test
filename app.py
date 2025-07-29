# STEP 1: Importing flask and inititalising the app
from flask import Flask, request, jsonify
app = Flask(__name__)
#                   ^^^
#     Flask: the main class for the app.
#     request: used to get data sent by the user (like name, or numbers).
#     jsonify: converts Python dictionaries to JSON responses (what APIs return).
#     app = Flask(__name__): creates an app instance.


# STEP 2: Creating the root route
@app.route('/')
def Hello():
    '''the function to run when / is accessed.'''
    return"Hello, Welcome to my API"
#                 ^^^
#   @app.route('/'): defines the route /.
#   hello(): the function to run when / is accessed.
#   return "Hello, Welcome...": sends a plain text response.


# STEP 3: Create a GET Endpoint - /greet
@app.route('/greet', methods=['GET'])
def greet():
    '''This will return a greeting using a name passed as a query parameter.'''
    name = request.args.get('name','Guest')
    return jsonify({'message': f'Hello, {name}!'})
#                 ^^^
#   @app.route('/greet', methods=['GET']): this route only accepts GET requests.
#   request.args.get('name', 'Guest'): looks for a query param like ?name=Amogh. If not found, uses 'Guest'.
#   jsonify(...): returns JSON like {"message": "Hello, Amogh!"}.

#   Example Usage:

#   Visit in browser:
#   http://127.0.0.1:5000/greet?name=Amogh

# STEP 4: Create a POST endpoint - /add
@app.route('/add', methods=['POST'])
def add():
    '''This will accept a JSON body with two numbers and return their sum'''
    data = request.get_json()
    result = data['a'] + data['b']
    return jsonify({'result': result})
#                 ^^^
#   request.get_json(): reads the JSON body sent in the POST request.
#   data['a'] + data['b']: adds the two values.
#   jsonify(...): returns {"result": 12} if a=5, b=7.

if (__name__) == ('__main__'):
    app.run(debug=True)
#                 ^^^
#   __name__ == '__main__': ensures this code runs when you do python app.py.
#   debug=True: enables hot-reloading (auto-restarts server on code change).