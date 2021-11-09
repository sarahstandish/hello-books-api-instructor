from app import db

class BookGenre(db.Model):

    book_id = db.Column(db.ForeignKey('book.id'))
    genre_id = db.Column(db.ForeignKey('genre.id'))