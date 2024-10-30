from models_postgres import User
from repositories.base_repository import BaseRepository
import psycopg2

class UsersPostgresRepository(BaseRepository):
    def get_all(self):
        con = psycopg2.connect(user='postgres', password='Opiskelijaolli98@', database='sovelluskehykset_bad1', port=5433)
        cur = con.cursor()
        cur.execute("SELECT * FROM users")
        result = cur.fetchall()
        users = [User(user[0], user[1], user[2], user[3]) for user in result]  # assuming id, username, firstname, lastname
        cur.close()
        con.close()
        return users

    def create_user(self, username, firstname, lastname):
        con = psycopg2.connect(user='postgres', password='Opiskelijaolli98@', database='sovelluskehykset_bad1',port=5433)
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
        con = psycopg2.connect(user='postgres', password='Opiskelijaolli98@', database='sovelluskehykset_bad1',
                               port=5433)
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
        con = psycopg2.connect(user='postgres', password='Opiskelijaolli98@', database='sovelluskehykset_bad1',
                               port=5433)
        cur = con.cursor()
        try:
            cur.execute("DELETE FROM users WHERE id = %s", (user_id,))
            con.commit()
        finally:
            cur.close()
            con.close()