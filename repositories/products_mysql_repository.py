from models_mysql import Product
from repositories.base_repository import BaseRepository
import mysql.connector

class ProductsMysqlRepository(BaseRepository):
    def get_all(self):
        con = mysql.connector.connect(user='root', database='sovelluskehykset_bad1')
        cur = con.cursor(dictionary=True)
        cur.execute("SELECT * FROM products")
        result = cur.fetchall()
        products = [Product(product['id'], product['name'], product['description']) for product in result]
        cur.close()
        con.close()
        return products
