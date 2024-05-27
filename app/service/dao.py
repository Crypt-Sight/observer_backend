from app.dao import BaseDAO
from app.service.model import UserModel


class UserDAO(BaseDAO):
    model = UserModel
