from flask import Flask
from flask_app.routes.main_route import bp as main_bp

app = Flask(__name__)
app.register_blueprint(main_bp)

@app.route('/', methods = ['POST', 'GET']) # => 127.0.0.1:5000 + / => 127.0.0.1:5000/
def index():
    dict_a = {
        'Hello' : 'Flask',
        'Bye' : ['a', 'b']
    }

    return dict_a, 201

@app.route('/user/', defaults = {'user_id' : 0})
@app.route('/user/<user_id>')
def user_index(user_id):
    return f"Here is your user id: {user_id}"

if __name__ == '__main__':
    app.run(debug=True)