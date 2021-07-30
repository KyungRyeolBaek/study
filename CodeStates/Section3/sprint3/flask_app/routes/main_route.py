from flask import Blueprint

# prefix 앞에 / 필수
bp = Blueprint('main', __name__, url_prefix='/main')

@bp.route('/') # => 127.0.0.1:5000 + '/main' + '/' => 127.0.0.1:5000/main/
def index():
    return 'Welcome to Main Index'