from app import db

class Genre(db.Model):
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    books = db.relationship("Book", secondary='bookgenre', back_populates="genres")

    def to_dict(self):

        return {
            "id": self.id,
            "name": self.name,
        }