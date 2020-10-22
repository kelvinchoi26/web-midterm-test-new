from flask import Flask, render_template, url_for, redirect, session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import os
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'some string'

app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Post(db.Model):
    __tablename__ = 'posts'
    postid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(64), unique=True)
    body = db.Column(db.String(64), unique=True)
    userid = db.Column(db.Integer, primary_key=True)
    users = db.relationship('User', backref='post', lazy='dynamic')

    def __repr__(self):
        return '<Post %r>' % self.title


class User(db.Model):
    __tablename__ = 'users'
    userid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.userid'), autoincrement=True)

    def __repr__(self):
        return '<User %r>' % self.name


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('go')


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/writing')
def writing():
    return render_template('writing.html')

@app.route('/board')
def board():
    return render_template('board.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':

    app.run()
