from models_mysql import User


def get_all_users():
    return User.get_all()


class UsersMysqlRepository:
    pass
