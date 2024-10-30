from models_mysql import User

class UsersMysqlRepository:
    def get_all_users(self):
        return User.get_all()
