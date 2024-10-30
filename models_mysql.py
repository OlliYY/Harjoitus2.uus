import mysql.connector


class User:
    def __init__(self, _id, username, firstname, lastname):
        self.id = _id
        self.username = username
        self.firstname = firstname
        self.lastname = lastname

    @classmethod
    def get_all(cls):
        with mysql.connector.connect(user='root', database='sovelluskehykset_bad1') as con:
            with con.cursor(dictionary=True) as cur:
                cur.execute('SELECT * FROM users')
                result = cur.fetchall()
                users = [cls(user['id'], user['username'], user['firstname'], user['lastname']) for user in result]
        return users
