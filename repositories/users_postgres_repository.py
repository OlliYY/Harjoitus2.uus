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
