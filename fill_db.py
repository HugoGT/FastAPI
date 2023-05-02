# File to fill the database

import csv

from sqlalchemy import Column, Integer, String, Float

from database import Base, Session, engine


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(250), nullable=True)
    subtitle = Column(String(250), nullable=True)
    authors = Column(String(250), nullable=True)
    categories = Column(String(250), nullable=True)
    published_year = Column(Integer, nullable=True)
    average_rating = Column(Float(10), nullable=True)
    num_pages = Column(Integer, nullable=True)
    ratings_count = Column(Integer, nullable=True)


# Filling the database
def run():
    Base.metadata.create_all(bind=engine)

    with open('database/books.csv', mode='r') as file:
        reader = csv.DictReader(file)
        db = Session()
        for row in reader:
            book = Book(**row)
            db.add(book)
        db.commit()
        db.close()


if __name__ == '__main__':
    run()
