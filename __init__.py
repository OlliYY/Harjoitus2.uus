
from flask import Flask


app = Flask(__name__)

from controllers.users import get_all_users
from controllers.products import get_all_products
