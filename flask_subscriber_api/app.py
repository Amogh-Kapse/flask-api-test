from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def Home():
    return "Welcome to the subcriber API"

@app.route('/subscribe' , methods = ['POST'])
def subscribe():
    data = request.get_json()

    if not data or 'email' not in data:
        return jsonify({"error": "email is required"}), 400
    
    email = data['email']

    # saving this email to a file.
    with open("subscribers.txt", "a") as f:
        f.write(email + "\n")
    
    return jsonify({"message": f"{email} saved successfully!"})

if __name__ == ('__main__'):
    app.run(debug=True)