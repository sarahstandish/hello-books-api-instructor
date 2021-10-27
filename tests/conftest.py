import pytest
from app import create_app
from app import db
from app.models.book import Book

@pytest.fixture
def app():
    app = create_app({ "TESTING" : True })
    with app.app_context():
        db.create_all()
        yield app
    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def two_saved_books(app):

    # Arrange
    ocean_book = Book(title="Ocean Book", description="Water")
    mountain_book = Book(title="Mountain Book", description="rocks")

    db.session.add_all([ocean_book, mountain_book])
    