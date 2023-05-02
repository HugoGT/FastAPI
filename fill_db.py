# File to fill the database

import csv

from sqlalchemy import Column, Integer, String, Float, Table, MetaData

from database import Base, Session, engine


meta = MetaData()

books = Table('books', meta,
    Column('id', Integer, primary_key=True),
    Column('title', String),
    Column('subtitle', String),
    Column('authors', String),
    Column('categories', String),
    Column('published_year', Integer),
    Column('average_rating', Float),
    Column('num_pages', Integer),
    Column('ratings_count', Integer)
)
Base.metadata.create_all(bind=engine)

# Filling the database
def run():
    with open('database/books.csv', mode='r') as file:
        reader = csv.DictReader(file)
        db = Session()
        for book in reader:
            db.execute(books.insert().values(**book))
            db.add(book)
        db.commit()
        db.close()


if __name__ == '__main__':
    run()
