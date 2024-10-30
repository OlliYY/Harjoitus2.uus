from flask import jsonify
from repositories.products_mysql_repository import ProductsMysqlRepository
from repositories.products_postgres_repository import ProductsPostgresRepository
# Voit vaihtaa ProductsMysqlRepository -> ProductsPostgresRepository tarvittaessa

def get_all_products():
    repo = ProductsPostgresRepository()
    #repo = ProductsMysqlRepository()
    products = repo.get_all()
    products_json = [
        {
            'id': product.id,
            'name': product.name,
            'description': product.description,
        }
        for product in products
    ]
    return jsonify(products_json)
