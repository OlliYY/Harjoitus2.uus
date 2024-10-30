## OLEN KÄYTTÄNYT TEHTÄVÄSSÄ APUNA TEKOÄLYÄ!
from flask import Flask

from controllers.users import get_all_users
from controllers.products import get_all_products


app = Flask(__name__)

app.add_url_rule('/api/users', 'get_all_users', get_all_users)
app.add_url_rule('/api/products', 'get_all_products', get_all_products)


if __name__ == '__main__':
    app.run()
