# from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_bootstrap import Bootstrap

# db = SQLAlchemy()
# migrate = Migrate()

# def create_app():
#     app = Flask(__name__)
#     app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://dxgkztoo:HN_JGJ6oqpaUwRFS9QGfwP2YNHwJCeZa@john.db.elephantsql.com/dxgkztoo"
#     db.init_app(app)
#     Bootstrap(app)
#     migrate.init_app(app, db)
    
#     @app.route('/', methods = ['GET'])
#     def sign_in():
#         return render_template('sign_in.html')

#     return app

# if __name__ == "__main__":
#     app = create_app()
#     app.run(debug=True) 


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     username = db.Column(db.String(30), nullable = True)
#     password = db.Column(db.String(30), nullable = True)
#     album = db.relationship('Album', backref = 'user', lazy = True)

#     def __repr__(self):
#         return f'User id : {self.id}, username : {self.username}'

# class Album(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     images = db.Column(db.String(100))
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

#     def __repr__(self):
#         return f'Album {self.id}'