from project.dao.models.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(Movie).get(uid)

    def get_all(self):
        return self.session.query(Movie).all()

    def get_by_director_id(self, value):
        return self.session.query(Movie).filter(Movie.director_id == value).all()

    def get_by_genre_id(self, value):
        return self.session.query(Movie).filter(Movie.genre_id == value).all()

    def get_by_year(self, value):
        return self.session.query(Movie).filter(Movie.year == value).all()

    def create(self, movie_a):
        ent = Movie(**movie_a)
        self.session.add(ent)
        self.session.commit()
        return ent

    def update(self, movie_a):
        movie = self.get_one(movie_a.get('id'))

        movie.title = movie_a.get("title")
        movie.description = movie_a.get("description")
        movie.trailer = movie_a.get("trailer")
        movie.year = movie_a.get("year")
        movie.rating = movie_a.get("rating")
        movie.genre_id = movie_a.get("genre_id")
        movie.director_id = movie_a.get("director_id")

        self.session.add(movie)
        self.session.commit()

    def delete(self, uid):
        movie = self.get_one(uid)

        self.session.delete(movie)
        self.session.commit()