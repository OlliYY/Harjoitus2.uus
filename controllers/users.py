from flask import jsonify

from models_mysql import User


# Nyt jokaista controlleria vastaa yksi tiedosto. Tiedostot sisältävät kaikki funktiot,jotka pitävät
# huolen requestin vastaanottamisesta ja responsen lähettämisestä.
def get_all_users():
    users =  User.get_all()
    users_json = []
    for user in users:
        users_json.append({
            'id': user.id,
            'username': user.username,
            'firstname': user.firstname,
            'lastname': user.lastname,
        })
    return jsonify(users_json)