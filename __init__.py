from flask import Flask
#from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@localhost:3306/exec'
    db.init_app(app)
    #Bootstrap(app)
    from app import models
    with app.app_context():
        db.create_all()
    return app


