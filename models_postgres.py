import psycopg2


class User:
    def __init__(self, _id, username, firstname, lastname):
        self.id = _id
        self.username = username
        self.firstname = firstname
        self.lastname = lastname

    @classmethod
    def get_all(cls):
        with psycopg2.connect(user='postgres', password='Opiskelijaolli98@', database='sovelluskehykset_bad1', port=5433) as con:
            with con.cursor() as cur:
                cur.execute('SELECT * FROM users')
                result = cur.fetchall()
                users = [cls(user[0], user[1], user[2], user[3]) for user in result]
        return users


class Product:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description
