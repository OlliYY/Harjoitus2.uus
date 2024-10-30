from models_postgres import User


def get_all_users():
    return User.get_all()


class UsersPostgresRepository:
    pass
