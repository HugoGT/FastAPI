# File to fill the database

import csv

from database import engine
from models import books


with open('database/books.csv', mode='r') as file:
    reader = csv.DictReader(file)

    conn = engine.connect()
    conn.begin()
    for book in reader:
        conn.execute(books.insert().values(book))
    conn.commit()
    conn.close()
