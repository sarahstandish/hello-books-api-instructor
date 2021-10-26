from flask import Blueprint, json, jsonify, make_response, request
from app import db
from app.models.book import Book

# group all the routes together in a route with a single prefix of books
books_bp = Blueprint("books", __name__, url_prefix="/books")

@books_bp.route("", methods=["POST", "GET"])
def handle_books():

    if request.method == "POST":
        request_body = request.get_json()

        if "title" not in request_body or "description" not in request_body:
            return "Invalid request", 400 # returning implicitly as a tuple (I hope)

        new_book = Book(
            title=request_body["title"],
            description=request_body["description"]
        )
        db.session.add(new_book)
        db.session.commit()
        return make_response(
            new_book.to_dict(),
            201
        )
    elif request.method == "GET":

        title = request.args.get("title")

        if title:
            books = Book.query.filter_by(title=title)
        
        else:
            books = Book.query.all()

        return jsonify([book.to_dict() for book in books])

@books_bp.route("/<book_id>", methods=["GET", "PUT", "DELETE"])
def handle_book(book_id):

    book = Book.query.get(book_id)
    if not book:
        return make_response(f"No book with id {book_id}.", 404)

    if request.method == "GET":
        return book.to_dict()

    elif request.method == "PUT":

        form_data = request.get_json()

        if not form_data:
            return "Update body must be included.", 400

        if "title" in form_data:
            book.title = form_data["title"]
        
        if "description" in form_data:
            book.description = form_data["description"]
        
        db.session.commit()

        return book.to_dict()

    elif request.method =="DELETE":
        
        db.session.delete(book)
        db.session.commit()
        return f"Book with id {book_id} deleted"