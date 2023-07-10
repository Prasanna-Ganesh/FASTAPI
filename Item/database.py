from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
import psycopg2


engine = create_engine("postgresql://postgres:postgres@localhost/item_db", echo=True)
Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)
