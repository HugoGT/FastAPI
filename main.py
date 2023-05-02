# Books API

from fastapi import FastAPI
from sqlalchemy import select, func, MetaData, Table, text

from database import Session, engine
from models import BookModel

app = FastAPI()
conn = Session()
meta = MetaData()

books = Table('books', meta)

from sqlalchemy import inspect
inspector = inspect(engine)
columns = inspector.get_columns('books')
print(columns)

@app.get("/")
def home():
    return {'message': 'Hola mundo!'}

# Books app
@app.get("/books")
def get_books():
    books = conn.execute(select(func.count()).select_from(books)).scalar()

    return {'message': f'Hay {books} libros'}

# Get a book by it's id
@app.get("/books/{book_id}")
def get_book(book_id: int):
    query = conn.execute(select("*").select_from(books).where(text(f"id = {book_id}"))).fetchone()

    if query == None:
        return {'book': f'No existe el libro con el id {book_id}'}

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

# Submit a book
@app.post("/books")
def add_book(book: BookModel):
    new_book = book.dict()

    try:
        conn.execute(books.insert().values(new_book))
    except Exception as e:
        return {'message': f'Error al insertar el libro: {e}'}

    return {'message': 'Libro insertado correctamente'}


# @user.put(
#     "users/{id}", tags=["users"], response_model=User, description="Update a User by Id"
# )
# def update_user(user: User, id: int):
#     conn.execute(
#         users.update()
#         .values(name=user.name, email=user.email, password=user.password)
#         .where(users.c.id == id)
#     )
#     return conn.execute(users.select().where(users.c.id == id)).first()


# @user.delete("/{id}", tags=["users"], status_code=HTTP_204_NO_CONTENT)
# def delete_user(id: int):
#     conn.execute(users.delete().where(users.c.id == id))
#     return conn.execute(users.select().where(users.c.id == id)).first()