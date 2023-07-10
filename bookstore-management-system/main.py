from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from passlib.context import CryptContext

from database import Base, engine
from models import Book

app = FastAPI()

# CORS settings
origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create database tables
Base.metadata.create_all(bind=engine)

# Configure session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Routes
@app.post("/books")
def create_book(book: Book):
    try:
        db.add(book)
        db.commit()
        db.refresh(book)
        return {"message": "Book created successfully", "book_id": book.id}
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Book with the same ISBN already exists")


@app.get("/books/{book_id}")
def get_book(book_id: int):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.query(Book).filter(Book.id == book_id).update(updated_book.dict(exclude_unset=True))
    db.commit()
    return {"message": "Book updated successfully"}


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()
    return {"message": "Book deleted successfully"}
