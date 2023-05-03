# Database config

import os

from sqlalchemy import create_engine, MetaData


meta = MetaData()

sqlite_filename = "../db.sqlite"
base_dir = os.path.dirname(os.path.realpath(__file__))

db_url = f"sqlite:///{os.path.join(base_dir, sqlite_filename)}"

engine = create_engine(db_url, echo=True, pool_size=20)
