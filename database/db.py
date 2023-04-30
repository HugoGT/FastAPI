# Database config

import csv
import os

from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker


sqlite_filename = "../db.sqlite"
base_dir = os.path.dirname(os.path.realpath(__file__))

db_url = f"sqlite:///{os.path.join(base_dir, sqlite_filename)}"

engine = create_engine(db_url, echo=True, pool_size=20)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


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


Base.metadata.create_all(bind=engine)

# Filling the database
with open('books.csv', mode='r') as file:
    reader = csv.DictReader(file)
    db = Session()
    for row in reader:
        book = Book(**row)
        db.add(book)
    db.commit()
    db.close()
