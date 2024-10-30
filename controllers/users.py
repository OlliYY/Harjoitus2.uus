from flask import jsonify
from repositories.users_mysql_repository import UsersMysqlRepository
from repositories.users_postgres_repository import UsersPostgresRepository


# Voi vaihtaa UsersMysqlRepository -> UsersPostgresRepository tarvittaessa
def get_all_users():
    repo = UsersPostgresRepository()
    #repo = UsersMysqlRepository()
    users = repo.get_all()
    users_json = [
    {
    'id': user.id,
    'username': user.username,
    'firstname': user.firstname,
    'lastname': user.lastname
    }
    for user in users
    ]
    return jsonify(users_json)