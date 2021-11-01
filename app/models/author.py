from flask.json import jsonify
from sqlalchemy.orm import relationship
from app import db

class Author(db.Model):

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(200))
    books = relationship("Book", back_populates="author")

    def to_dict(self):
        from .book import Book

        books = Book.query.filter_by(author_id = self.id)

        return {
            "id" : self.id,
            "name" : self.name,
            "books" : [book.to_dict() for book in books]
        }
