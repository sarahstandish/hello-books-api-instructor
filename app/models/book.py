from app import db


class Book(db.Model):
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    author = db.relationship("Author", back_populates="books")

    def to_dict(self):
        from .author import Author

        author = Author.query.get(self.author_id)

        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "author_id" : self.author_id,
            "author": author.to_dict()
        }