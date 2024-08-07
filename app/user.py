from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from app.models import User, db

user_bp = Blueprint('user', __name__)

@user_bp.route('/profile', methods=['GET', 'PUT'])
@jwt_required()
def profile():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    if request.method == 'GET':
        if user:
            return jsonify({'first_name':user.first_name, 'other_names':user.other_names, 'last_name':user.last_name, 'username': user.username, 'email': user.email, 'address': user.address, 'phone_number': user.phone_number}), 200
        else:
            return jsonify({'message': 'User not found'}), 404
    elif request.method == 'PUT':
        data = request.get_json()
        user.username = data['username']
        user.email = data['email']
        user.address = data['address']
        user.phone_number = data['phone_number']
        user.last_name = data['last_name']
        user.other_names = data['other_names']
        user.first_name = data['first_name']
        db.session.commit()
        return jsonify({'message': 'Profile updated successfully'}), 200