from . import auth
from flask import request, jsonify
from app.models import User
from werkzeug.security import check_password_hash


@auth.route('/signup', methods=['POST'])
def sign_up():
    data = request.json
    new_user = User(
        first_name = data['first_name'],
        last_name=data['last_name'],
        email=data['email'],
        username=data['username'],
        phone_number=data['phone_number'],
        password=data['password']
    )
    checkUser = User.query.filter(User.username == new_user.username).first()
    checkPhoneNumber = User.query.filter(User.phone_number == new_user.phone_number).first()
    checkEmail = User.query.filter(User.email == new_user.email).first()
    if checkUser:
        return jsonify({"message": "Username already exists "}) , 400
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
            return jsonify({'message': "Login Successful"}), 201
        else: 
            return jsonify({"message": "Login failed"}), 400


