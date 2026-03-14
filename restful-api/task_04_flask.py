from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory dictionary to store users
users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def get_data():
    # Return a JSON list of all the usernames (keys of the dictionary)
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    return "OK"

@app.route("/users/<username>")
def get_user(username):
    # Retrieve the user object if the username exists
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        # User not found
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    # Parse the incoming JSON data
    data = request.get_json(silent=True)

    # Check if the request body is valid JSON
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    # Extract the username
    username = data.get("username")

    # Check if the username is provided
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Check for duplicate usernames (Optional based on instructions, but good for expected outputs)
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Add new user to dictionary
    users[username] = data

    # Return confirmation message and data
    return jsonify({
        "message": "User added",
        "user": data
    }), 201

if __name__ == "__main__":
    app.run()
