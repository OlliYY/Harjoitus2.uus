## OLEN KÄYTTÄNYT TEHTÄVÄSSÄ APUNA TEKOÄLYÄ!
from flask import Flask

from controllers.users import get_all_users

app = Flask(__name__)

app.add_url_rule('/api/users', 'get_all_users', get_all_users)

if __name__ == '__main__':
    app.run()
