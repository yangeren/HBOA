from flask import Flask
import sqlite3
import datetime
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you never know'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + 'HBOA.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)


class OaDb(db.Model):

    __tablename = 'oadb'
    id = db.Column(db.Integer)
    position = db.Column(db.String(200))
    createTime = db.Column(db.DateTime)
    comp = db.Column(db.String(200))
    itemname = db.Column(db.String(200))
    dostat = db.Column(db.String(20))
    cityname = db.Column(db.String(64))
    casedate = db.Column(db.DateTime)
    citycode = db.Column(db.String(10))
    workname = db.Column(db.String(64))
    showcode = db.Column(db.String(64), primary_key=True)
    domain = db.Column(db.Integer)
    commitman = db.Column(db.String(64))
    userphone = db.Column(db.String(32))
    itemdate = db.Column(db.DateTime)
    itemcode = db.Column(db.String(32))


if __name__ == '__main__':
    pass