from flask import request
from flask_restx import Resource, Namespace

from project.dao.models.genre import GenreSchema
from project.decorator import admin_required, auth_required
from project.implemented import genre_service

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    @auth_required
    def get(self):
        page = request.args.get("page")
        filters = {"page": page}
        genre = genre_service.get_all(filters)
        result = GenreSchema(many=True).dump(genre)
        return result, 200

    @admin_required
    def post(self):
        request_json = request.json
        genre = genre_service.create(request_json)
        return "", 201, {"location": f"/genres/{genre.id}"}


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    @auth_required
    def get(self, gid):
        genre = genre_service.get_one(gid)
        result = GenreSchema().dump(genre)
        return result, 200

    @admin_required
    def put(self, gid):
        request_json = request.json
        if "id" not in request_json:
            request_json["id"] = gid

        genre_service.update(request_json)
        return "", 204

    @admin_required
    def delete(self, gid):
        genre_service.delete(gid)
        return "", 2014
