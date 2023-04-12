from flask import request
from flask_restx import Resource, Namespace

from project.dao.models.director import DirectorSchema
from project.decorator import auth_required, admin_required
from project.implemented import director_service

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    @auth_required
    def get(self):
        page = request.args.get("page")
        filters = {"page": page}
        director = director_service.get_all(filters)
        result = DirectorSchema(many=True).dump(director)
        return result, 200

    @admin_required
    def post(self):
        request_json = request.json
        director = director_service.create(request_json)
        return "", 201, {"location": f"/directors/{director.id}"}


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    @auth_required
    def get(self, did):
        director = director_service.get_one(did)
        result = DirectorSchema().dump(director)
        return result, 200

    @admin_required
    def put(self, did):
        request_json = request.json
        if "id" not in request_json:
            request_json["id"] = did

        director_service.update(request_json)
        return "", 204

    @admin_required
    def delete(self, did):
        director_service.delete(did)
        return "", 2014