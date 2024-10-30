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