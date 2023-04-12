from project.dao.models.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(Genre).get(uid)

    def get_all(self):
        return self.session.query(Genre).all()

    def create(self, genre_a):
        ent = Genre(**genre_a)
        self.session.add(ent)
        self.session.commit()
        return ent

    def update(self, genre_a):
        genre = self.get_one(genre_a.get('id'))

        genre.name = genre_a.get('name')

        self.session.add(genre)
        self.session.commit()

    def delete(self, uid):
        genre = self.get_one(uid)

        self.session.delete(genre)
        self.session.commit()