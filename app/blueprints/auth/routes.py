from . import auth
from flask import request, jsonify
from flask_login import login_required, logout_user, login_user
from app.models import User
from werkzeug.security import check_password_hash


@auth.route('/signup', methods=['POST'])
def sign_up():
    data = request.json
    new_user = User(
        first_name = data['first_name'],
        last_name=data['last_name'],
        email=data['email'],
        company_name=data['company_name'],
        phone_number=data['phone_number'],
        password=data['password'],
    )
    checkUser = User.query.filter(User.company_name == new_user.company_name).first()
    checkPhoneNumber = User.query.filter(User.phone_number == new_user.phone_number).first()
    checkEmail = User.query.filter(User.email == new_user.email).first()
    if checkUser:
        return jsonify({"message": "Company Name already exists "}) , 400
    if checkEmail:
        return jsonify({"message": "Email already in use"}), 400
    if checkPhoneNumber: 
        return jsonify({"message": "Phone Number already in use"}), 400
    if len(data['password']) < 7:
        return jsonify({"message": "Password must be at least 7 characters"}), 400
    new_user.save()
    return jsonify({'message': "User created successfully"}), 201

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")
        user = User.query.filter(User.email == email).first()
        if user and check_password_hash(user.password, password):
            return jsonify({'message': "Login Successful", "user": user.to_dict()}), 201
        else: 
            return jsonify({"message": "Login failed"}), 400


@auth.route("/logout", methods=["POST"])
def logout():
    return jsonify({"message": "Logout successful"}), 200
        
@auth.route("/login_status/<email>")
def get_login_status(email):
    user = User.query.filter(User.email == email).first()
    if user:
        return jsonify({'logged_in': True}), 200
    else:
        return jsonify({'logged_in': False}), 200





