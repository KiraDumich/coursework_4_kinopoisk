from flask_restx import Resource, Namespace
from flask import request

from project.dao.models.user import UserSchema
from project.implemented import user_service

user_ns = Namespace('users')


@user_ns.route('/')
class UsersView(Resource):
    def get(self):
        all_users = user_service.get_all()
        result = UserSchema(many=True).dump(all_users)
        return result, 200

    def post(self):
        request_json = request.json
        user = user_service.create(request_json)
        return "", 201, {"location": f"/users/{user.id}"}


@user_ns.route('/<int:uid>')
class UserView(Resource):
    def get(self, uid):
        user = user_service.get_one(uid)
        result = UserSchema().dump(user)
        return result, 200

    def patch(self, uid):
        request_json = request.json
        if "id" not in request_json:
            request_json["id"] = uid

        user_service.update(request_json)
        return "", 204

    def delete(self, uid):
        user_service.delete(uid)
        return "", 204


@user_ns.route('/password')
class UpdateUserPassword(Resource):
    def put(self):
        request_json = request.json
        email = request_json.get("email")
        old_password = request_json.get("password_1")
        new_password = request_json.get("password_2")
        user = user_service.get_by_email(email)
        if user_service.compare_passwords(user.password, old_password):
            user.password = user_service.get_hash(new_password)
            result = UserSchema().dump(user)
            user_service.update(result)
        else:
            print("Пароль не изменился")

        return "", 201
