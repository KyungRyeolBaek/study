import re, os
from flask import Flask, render_template, redirect, url_for, request
from flask.helpers import make_response
from flask.json import jsonify
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy  import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SECRET_KEY'] = '6a3261c2-2fa2-4254-8d74-17f305e4403c'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://dxgkztoo:HN_JGJ6oqpaUwRFS9QGfwP2YNHwJCeZa@john.db.elephantsql.com:5432/dxgkztoo"
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate()
migrate.init_app(app, db)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(15), unique=True, nullable = True)
    email = db.Column(db.String(50), unique=True, nullable = True)
    password = db.Column(db.String(100))
    album = db.relationship('Album', backref = 'user', lazy = True)

    def __repr__(self):
        return f'User id : {self.id}, username : {self.username}'

class Album(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    images = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'Album {self.id}'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=100)])
    remember = BooleanField('remember me')

class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=100)])


app.config['UPLOAD_FOLDER'] = "C:/Users/forev/PycharmProjects/study/CodeStates/Section3/Section3_Project/kyungryeol_app/app/static/upload"

@app.route('/', methods=['GET', 'POST'])
def index():

    return render_template('index.html')

import pandas as pd
import matplotlib.pyplot as plt
@app.route('/album', methods=['GET', 'POST'])
@login_required
def upload():
    filename = None

    if request.method == "POST":
        filesize = request.cookies.get("filesize")
        file = request.files["file"]
        filename = file.filename
        filename_ori = filename.split('.')[0]

        print(f"Filesize: {filesize}")
        print(file)

        res = make_response(jsonify({"message": f"{file.filename} uploaded"}), 200)
        
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        df = pd.read_csv(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        plt.imshow(df)
        plt.savefig(os.path.join(app.config['UPLOAD_FOLDER'], '{}.jpg'.format(filename_ori)))
        plt.clf()
        return res

    return render_template('album.html', filename = filename)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            # if check_password_hash(user.password, form.password.data):
            if user.password == form.password.data:
                login_user(user, remember=form.remember.data)
                return redirect(url_for('dashboard'))

        return '<h1>아이디가 일치하지 않습니다.</h1>'
        # return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'

    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        # hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(new_user)
        db.session.commit()

        return render_template('signup_alert.html', form=form)
        # return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'

    return render_template('signup.html', form=form)

@app.route('/dashboard')
@login_required
def dashboard():
    global name
    name = current_user.username
    return render_template('dashboard.html', name=current_user.username)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/signup', methods = ["GET", "POST"])
def signup_alert():
    form = RegisterForm()

    if form.validate_on_submit():
        return render_template('index')

@app.route('/images', methods = ["GET", "POST"])
def images():
    return render_template('images.html')

@app.route('/result', methods = ["GET", "POST"])
def result():
    filename = None

    if request.method == "POST":
        file = request.files["file"]
        filename = file.filename
        filename_ori = filename.split('.')[0]

        filesize = request.cookies.get("filesize")

        print(f"Filesize: {filesize}")
        print(file)

        res = make_response(jsonify({"message": f"{file.filename} uploaded"}), 200)
        
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        df = pd.read_csv(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        plt.imshow(df)
        plt.savefig(os.path.join(app.config['UPLOAD_FOLDER'], '{}.jpg'.format(filename_ori)))
        plt.clf()
        return res

    return render_template('result.html', filename = filename)


@app.route('/model_train', methods = ["GET", "POST"])
def model():
    if request.method == "POST":
        from sub_dir import df_result
        result = df_result
        plt.imshow(result)
        plt.savefig(os.path.join(app.config['UPLOAD_FOLDER'], 'result_img.jpg'))
        plt.clf()

        res = make_response(jsonify({"message": "Model Trainde, \n test_loss = , test_acc = "}), 200)

        return res

    return render_template('model_train.html')

@app.route('/delete_id')
def delete_id():
    user = db.session.query(User).filter(User.username == name).first()
    db.session.delete(user)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/add_album', methods = ["GET", "POST"])
def add_album(album_name):
    new_album = db.session.query(User).filter(User.username == name).first()
    add_album = Album(user_id = new_album, images = album_name)
    db.session.add(add_album)
    db.session.commit()

    return render_template('album.html')

if __name__ == '__main__':
    app.run(debug=True)
