from flask import jsonify, request
from repositories.products_mysql_repository import ProductsMysqlRepository
from repositories.products_postgres_repository import ProductsPostgresRepository

# Valitse käytettävä tietokanta
# repo = ProductsMysqlRepository()  # MySQL
repo = ProductsPostgresRepository()  # PostgreSQL

def get_all_products():
    products = repo.get_all()
    products_json = [
        {
            'id': product.id,
            'name': product.name,
            'description': product.description
        }
        for product in products
    ]
    return jsonify(products_json)

def create_product():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    repo.create_product(name, description)
    return jsonify({"message": "Product created successfully"}), 201

def update_product(product_id):
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    repo.update_product(product_id, name, description)
    return jsonify({"message": "Product updated successfully"}), 200

def delete_product(product_id):
    repo.delete_product(product_id)
    return jsonify({"message": "Product deleted successfully"}), 200

