from models_postgres import User

class UsersPostgresRepository:
    def get_all_users(self):
        return User.get_all()
