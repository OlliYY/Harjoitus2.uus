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
            with con.cursor() as cur:
                cur.execute('SELECT * FROM users')
                result = cur.fetchall()
                users = []
                for user in result:
                    users.append(cls(user[0], user[1], user[2], user[3]))

                return users