from models_mysql import User
from repositories.base_repository import BaseRepository
import mysql.connector

class UsersMysqlRepository(BaseRepository):
    def get_all(self):
        con = mysql.connector.connect(user='root', database='sovelluskehykset_bad1')
        cur = con.cursor(dictionary=True)
        cur.execute("SELECT * FROM users")
        result = cur.fetchall()
        users = [User(user['id'], user['username'], user['firstname'], user['lastname']) for user in result]
        cur.close()
        con.close()
        return users

    def create_user(self, username, firstname, lastname):
        con = mysql.connector.connect(user='root', database='sovelluskehykset_bad1')
        cur = con.cursor()
        try:
            cur.execute(
                "INSERT INTO users (username, firstname, lastname) VALUES (%s, %s, %s)",
                (username, firstname, lastname)
            )
            con.commit()
        finally:
            cur.close()
            con.close()

    def update_user(self, user_id, username, firstname, lastname):
        con = mysql.connector.connect(user='root', database='sovelluskehykset_bad1')
        cur = con.cursor()
        try:
            cur.execute(
                "UPDATE users SET username = %s, firstname = %s, lastname = %s WHERE id = %s",
                (username, firstname, lastname, user_id)
            )
            con.commit()
        finally:
            cur.close()
            con.close()

    def delete_user(self, user_id):
        con = mysql.connector.connect(user='root', database='sovelluskehykset_bad1')
        cur = con.cursor()
        try:
            cur.execute("DELETE FROM users WHERE id = %s", (user_id,))
            con.commit()
        finally:
            cur.close()
            con.close()