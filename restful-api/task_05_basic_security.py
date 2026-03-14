from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)

app = Flask(__name__)

# Basic Auth configuration
auth = HTTPBasicAuth()

# JWT configuration
app.config['JWT_SECRET_KEY'] = 'a_very_secret_key_for_testing'  # Change this in production
jwt = JWTManager(app)

# User Data
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

# --- Basic Authentication --- #

@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return username
    return None

@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


# --- JWT Authentication --- #

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json(silent=True)
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({"error": "Missing credentials"}), 400

    username = data.get('username')
    password = data.get('password')

    user = users.get(username)

    # Check if user exists and password is correct
    if user and check_password_hash(user['password'], password):
        # Create token with username as identity and embed role in additional claims
        access_token = create_access_token(
            identity=username,
            additional_claims={"role": user['role']}
        )
        return jsonify({"access_token": access_token}), 200

    return jsonify({"error": "Invalid credentials"}), 401

@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"

@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    user_role = users.get(current_user, {}).get("role")

    if user_role != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


# --- JWT Error Handlers --- #

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == '__main__':
    app.run()
