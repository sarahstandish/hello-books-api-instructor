from app import db

class Book(db.Model):
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    author = db.relationship("Author", back_populates="books")
    genres = db.relationship("Genre", secondary='books_genres', back_populates="books")

    def to_dict(self):

        return {
            "book id": self.id,
            "title": self.title,
            "description": self.description,
            "author": self.author.name if self.author_id else None,
            "genre(s)": [genre.to_dict() for genre in self.genres] if self.genres else None
        }