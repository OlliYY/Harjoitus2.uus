## OLEN KÄYTTÄNYT TEHTÄVÄSSÄ APUNA TEKOÄLYÄ!
from flask import Flask
from controllers.users import get_all_users, create_user, update_user, delete_user
from controllers.products import get_all_products, create_product, update_product, delete_product

app = Flask(__name__)

# Määritä käyttäjäreitit
app.add_url_rule('/api/users', 'get_all_users', get_all_users, methods=['GET'])
app.add_url_rule('/api/users', 'create_user', create_user, methods=['POST'])
app.add_url_rule('/api/users/<int:user_id>', 'update_user', update_user, methods=['PUT'])
app.add_url_rule('/api/users/<int:user_id>', 'delete_user', delete_user, methods=['DELETE'])

# Määritä tuotejäreitit
app.add_url_rule('/api/products', 'get_all_products', get_all_products, methods=['GET'])
app.add_url_rule('/api/products', 'create_product', create_product, methods=['POST'])
app.add_url_rule('/api/products/<int:product_id>', 'update_product', update_product, methods=['PUT'])
app.add_url_rule('/api/products/<int:product_id>', 'delete_product', delete_product, methods=['DELETE'])

if __name__ == '__main__':
    app.run()
