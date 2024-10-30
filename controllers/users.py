from flask import jsonify, request
from repositories.users_mysql_repository import UsersMysqlRepository
from repositories.users_postgres_repository import UsersPostgresRepository

# Valitse käytettävä tietokanta
# repo = UsersMysqlRepository()  # MySQL
repo = UsersPostgresRepository()  # PostgreSQL

def get_all_users():
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

def create_user():
    data = request.get_json()
    username = data.get('username')
    firstname = data.get('firstname')
    lastname = data.get('lastname')
    repo.create_user(username, firstname, lastname)
    return jsonify({"message": "User created successfully"}), 201

def update_user(user_id):
    data = request.get_json()
    username = data.get('username')
    firstname = data.get('firstname')
    lastname = data.get('lastname')
    repo.update_user(user_id, username, firstname, lastname)
    return jsonify({"message": "User updated successfully"}), 200

def delete_user(user_id):
    repo.delete_user(user_id)
    return jsonify({"message": "User deleted successfully"}), 200
