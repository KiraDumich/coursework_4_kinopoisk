import base64
import hashlib
import hmac

from project.dao.user import UserDAO
from project.constants import PWD_HASH_ITERATIONS, PWD_HASH_SALT


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_all(self):
        return self.dao.get_all()

    def get_by_email(self, email):
        return self.dao.get_by_email(email)

    def create(self, user_d):
        user_d["password"] = self.get_hash(user_d.get("password"))
        return self.dao.create(user_d)

    def update(self, user_d):
        self.dao.update(user_d)
        return self.dao

    def delete(self, uid):
        self.dao.delete(uid)

    def get_hash(self, password):
        return base64.b64encode(hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        ))

    def compare_passwords(self, password_hash, request_password):
        return hmac.compare_digest(
            base64.b64decode(password_hash),
            hashlib.pbkdf2_hmac('sha256',
                                request_password.encode('utf-8'),
                                PWD_HASH_SALT,
                                PWD_HASH_ITERATIONS)
        )