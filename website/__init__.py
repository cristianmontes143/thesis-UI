from flask import Flask
from .models import db
from .views import views

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '2'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:iLOVEyou143@localhost:5432/thesis_data'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(views, url_prefix='/')

    return app
