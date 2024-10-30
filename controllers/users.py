from flask import jsonify
from repositories.users_mysql_repository import UsersMysqlRepository
from repositories.users_postgres_repository import UsersPostgresRepository


# Nyt jokaista controlleria vastaa yksi tiedosto. Tiedostot sisältävät kaikki funktiot,jotka pitävät
# huolen requestin vastaanottamisesta ja responsen lähettämisestä.
def get_all_users():
    repo = UsersPostgresRepository()
    #repo = UsersMysqlRepository() #Muutetaan tarvittaessa PostgreSQL käyttämiseen
    users = repo.get_all_users()
    users_json = [{
    'id': user.id,
    'username': user.username,
    'firstname': user.firstname,
    'lastname': user.lastname}
    for user in users]
    return jsonify(users_json)