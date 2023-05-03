# Book model

from sqlalchemy import Table, Column, Integer, String, Float

from database import meta, engine


books = Table('books', meta,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('title', String(255), nullable=True),
    Column('subtitle', String(255), nullable=True),
    Column('authors', String(255), nullable=True),
    Column('categories', String(255), nullable=True),
    Column('published_year', Integer, nullable=True),
    Column('average_rating', Float, nullable=True),
    Column('num_pages', Integer, nullable=True),
    Column('ratings_count', Integer, nullable=True)
)

meta.create_all(engine)