from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

load_dotenv()

db = SQLAlchemy()
migrate = Migrate()

def create_app(test_config=None):
    app = Flask(__name__)

    connection_string = os.environ.get("SQLALCHEMY_DATABASE_URI") if test_config else os.environ.get("SQLALCHEMY_TEST_DATABASE_URI")

    if test_config:
        app.config["TESTING"]

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config['SQLALCHEMY_DATABASE_URI'] = connection_string

    db.init_app(app)
    migrate.init_app(app, db)
    from app.models.book import Book

    from .routes import books_bp
    app.register_blueprint(books_bp)

    return app
