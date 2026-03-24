from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.db.db import SessionLocal
from app.db import crud
from app import schemas

router = APIRouter(prefix="/books", tags=["Books"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[schemas.BookResponse])
def list_books(
    category_id: int | None = Query(None),
    db: Session = Depends(get_db)
):
    books = crud.get_books(db)

    if category_id:
        books = [b for b in books if b.category_id == category_id]

    return books


@router.get("/{book_id}", response_model=schemas.BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book(db, book_id)
    if not book:
        raise HTTPException(404, "Book not found")
    return book


@router.post("/", response_model=schemas.BookResponse, status_code=201)
def create_book(data: schemas.BookCreate, db: Session = Depends(get_db)):
    category = crud.get_category(db, data.category_id)
    if not category:
        raise HTTPException(400, "Category does not exist")

    return crud.create_book(
        db,
        title=data.title,
        description=data.description,
        price=data.price,
        category_id=data.category_id,
        url=data.url
    )


@router.put("/{book_id}", response_model=schemas.BookResponse)
def update_book(book_id: int, data: schemas.BookUpdate, db: Session = Depends(get_db)):
    if data.category_id:
        category = crud.get_category(db, data.category_id)
        if not category:
            raise HTTPException(400, "Category does not exist")

    book = crud.update_book(
        db,
        book_id,
        title=data.title,
        description=data.description,
        price=data.price,
        category_id=data.category_id,
        url=data.url
    )

    if not book:
        raise HTTPException(404, "Book not found")

    return book


@router.delete("/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.delete_book(db, book_id)
    if not book:
        raise HTTPException(404, "Book not found")
    return {"message": "Book deleted"}