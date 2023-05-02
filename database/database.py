# Database config

import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker


sqlite_filename = "../db.sqlite"
base_dir = os.path.dirname(os.path.realpath(__file__))

db_url = f"sqlite:///{os.path.join(base_dir, sqlite_filename)}"

engine = create_engine(db_url, echo=True, pool_size=20)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
