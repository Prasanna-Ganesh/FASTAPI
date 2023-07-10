from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# from sqlalchemy.dialects import psycopg2


SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost/user_db"
engine = create_engine(SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
