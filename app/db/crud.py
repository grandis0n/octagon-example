from sqlalchemy.orm import Session
from . import models


# ======================
# CATEGORY CRUD
# ======================

def create_category(db: Session, title: str):
    category = models.Category(title=title)
    db.add(category)
    db.commit()
    db.refresh(category)
    return category


def get_category(db: Session, category_id: int):
    return db.query(models.Category).filter(
        models.Category.id == category_id
    ).first()


def get_categories(db: Session):
    return db.query(models.Category).all()


def update_category(db: Session, category_id: int, title: str):
    category = get_category(db, category_id)
    if category:
        category.title = title
        db.commit()
        db.refresh(category)
    return category


def delete_category(db: Session, category_id: int):
    category = get_category(db, category_id)
    if category:
        db.delete(category)
        db.commit()
    return category


# ======================
# BOOK CRUD
# ======================

def create_book(
    db: Session,
    title: str,
    description: str,
    price: float,
    category_id: int,
    url: str = ""
):
    book = models.Book(
        title=title,
        description=description,
        price=price,
        category_id=category_id,
        url=url
    )
    db.add(book)
    db.commit()
    db.refresh(book)
    return book


def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(
        models.Book.id == book_id
    ).first()


def get_books(db: Session):
    return db.query(models.Book).all()


def update_book(
    db: Session,
    book_id: int,
    title: str = None,
    description: str = None,
    price: float = None,
    category_id: int = None,
    url: str = None
):
    book = get_book(db, book_id)
    if book:
        if title is not None:
            book.title = title
        if description is not None:
            book.description = description
        if price is not None:
            book.price = price
        if category_id is not None:
            book.category_id = category_id
        if url is not None:
            book.url = url

        db.commit()
        db.refresh(book)
    return book


def delete_book(db: Session, book_id: int):
    book = get_book(db, book_id)
    if book:
        db.delete(book)
        db.commit()
    return book