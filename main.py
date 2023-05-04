# Books API

from fastapi import FastAPI
from sqlalchemy import text, select, func
from typing import Any, Dict

from database import engine
from models import books
from schemas import Book


app = FastAPI()
conn = engine.connect()


@app.get("/")
def home():
    return {'message': 'Hola mundo!'}

# Books app
@app.get("/books")
def get_books():
    query = conn.execute(select(func.count()).select_from(books)).scalar()

    return {'message': f'Hay {query} libros'}

# Submit a book
@app.post("/books")
def add_book(book: Book):
    new_book = book.dict()

    try:
        result = conn.execute(books.insert().values(new_book))
        conn.commit()
    except Exception as e:
        return {'message': f'Error al insertar el libro: {e}'}

    new_book['id'] = result.lastrowid

    return {
        'message': 'Libro agregado correctamente',
        'book': new_book
        }

# Get a book by it's id
@app.get("/books/{book_id}")
def get_book(book_id: int):
    query = conn.execute(select("*").select_from(books).where(text(f"id = {book_id}"))).fetchone()

    if query == None:
        return {'message': f'No existe el libro con el id {book_id}'}

    book = {
        'id': query[0],
        'title': query[1],
        'subtitle': query[2],
        'authors': query[3],
        'categories': query[4],
        'published_year': query[5],
        'average_rating': query[6],
        'num_pages': query[7],
        'ratings_count': query[8]
    }

    return {'book': book}

# Delete a book by it's id
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    query = conn.execute(books.delete().where(books.c.id == book_id))
    conn.commit()

    if query.rowcount == 0:
        return {'message': f'No existe el libro con el id {book_id}'}

    return {'message': 'Libro eliminado con éxito'}

# Update a book
@app.patch("/books/{book_id}")
def update_book(book_id: int, fields: Dict[str, Any]):
    query = conn.execute(books.update().values(**fields).where(books.c.id == book_id))
    conn.commit()

    if query.rowcount == 0:
        return {'message': f'No existe el libro con el id {book_id}'}

    return {'message': f'Libro {book_id} actualizado con éxito'}
