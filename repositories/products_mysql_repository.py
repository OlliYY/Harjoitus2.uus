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

    def create_product(self, name, description):
        con = mysql.connector.connect(user='root', database='sovelluskehykset_bad1')
        cur = con.cursor()
        try:
            cur.execute(
                "INSERT INTO products (name, description) VALUES (%s, %s)",
                (name, description)
            )
            con.commit()
        finally:
            cur.close()
            con.close()

    def update_product(self, product_id, name, description):
        con = mysql.connector.connect(user='root', database='sovelluskehykset_bad1')
        cur = con.cursor()
        try:
            cur.execute(
                "UPDATE products SET name = %s, description = %s WHERE id = %s",
                (name, description, product_id)
            )
            con.commit()
        finally:
            cur.close()
            con.close()

    def delete_product(self, product_id):
        con = mysql.connector.connect(user='root', database='sovelluskehykset_bad1')
        cur = con.cursor()
        try:
            cur.execute("DELETE FROM products WHERE id = %s", (product_id,))
            con.commit()
        finally:
            cur.close()
            con.close()
