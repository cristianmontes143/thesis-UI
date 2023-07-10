from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Thesis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    abstract = db.Column(db.Text)
