from project.dao.models.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(Director).get(uid)

    def get_all(self):
        return self.session.query(Director).all()

    def create(self, director_a):
        ent = Director(**director_a)
        self.session.add(ent)
        self.session.commit()
        return ent

    def update(self, director_a):
        director = self.get_one(director_a.get('id'))

        director.name = director_a.get('name')

        self.session.add(director)
        self.session.commit()

    def delete(self, uid):
        director = self.get_one(uid)

        self.session.delete(director)
        self.session.commit()