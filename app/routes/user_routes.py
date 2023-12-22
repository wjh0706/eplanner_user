from flask import Blueprint, request, jsonify
from ..services.user_service import get_user_info, update_user_info, update_user_photo, create_user

user_blueprint = Blueprint('user_blueprint', __name__)

@user_blueprint.route('/')
def users_index():
    return 'User-specific Index Page'

@user_blueprint.route('/api/user/<int:userid>/info', methods=['GET', 'PUT'])
def user_info(userid):
    if request.method == 'GET':
        return jsonify(get_user_info(userid))
    elif request.method == 'PUT':
        # Assumes JSON data in request
        data = request.json
        return jsonify(update_user_info(userid, data))

@user_blueprint.route('/api/user/<int:userid>/photo', methods=['PUT'])
def user_photo(userid):
    # Assuming file is sent in request
    file = request.json
    return jsonify(update_user_photo(userid, file))

@user_blueprint.route('/api/user/create', methods=['POST'])
def user_create():
    data = request.json
    result = create_user(data)
    return jsonify(result)
