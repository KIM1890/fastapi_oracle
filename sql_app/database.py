from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists

# path to sqlite3
SQLALCHEMY_DATABASE_URL = 'sqlite:///./sql_app.db'
# create engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})
# check database exists
# database_exists(engine.url)
# call to sessionmaker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# create Base for model
Base = declarative_base()
