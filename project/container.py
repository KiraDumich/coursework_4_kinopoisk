from project.dao.genre import GenreDAO

from project.services.genre import GenreService
from project.setup.db import db

# DAO
genre_dao = GenreDAO(db.session)

# Services
genre_service = GenreService(dao=genre_dao)
