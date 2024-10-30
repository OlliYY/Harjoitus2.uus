from models_postgres import Product
from repositories.base_repository import BaseRepository
import psycopg2

class ProductsPostgresRepository(BaseRepository):
    def get_all(self):
        con = psycopg2.connect(user='postgres', password='Opiskelijaolli98@', database='sovelluskehykset_bad1', port=5433)
        cur = con.cursor()
        cur = con.cursor()
        cur.execute("SELECT * FROM products")
        result = cur.fetchall()
        products = [Product(product[0], product[1], product[2]) for product in result]  # assuming id, name, description
        cur.close()
        con.close()
        return products

    def create_product(self, name, description):
        con = psycopg2.connect(user='postgres', password='Opiskelijaolli98@', database='sovelluskehykset_bad1',port=5433)
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
        con = psycopg2.connect(user='postgres', password='Opiskelijaolli98@', database='sovelluskehykset_bad1',
                               port=5433)
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
        con = psycopg2.connect(user='postgres', password='Opiskelijaolli98@', database='sovelluskehykset_bad1',
                               port=5433)
        cur = con.cursor()
        try:
            cur.execute("DELETE FROM products WHERE id = %s", (product_id,))
            con.commit()
        finally:
            cur.close()
            con.close()