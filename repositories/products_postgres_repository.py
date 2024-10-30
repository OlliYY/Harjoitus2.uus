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
