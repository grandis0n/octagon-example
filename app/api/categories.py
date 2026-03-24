from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.db import SessionLocal
from app.db import crud
from app import schemas

router = APIRouter(prefix="/categories", tags=["Categories"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[schemas.CategoryResponse])
def list_categories(db: Session = Depends(get_db)):
    return crud.get_categories(db)


@router.get("/{category_id}", response_model=schemas.CategoryResponse)
def get_category(category_id: int, db: Session = Depends(get_db)):
    category = crud.get_category(db, category_id)
    if not category:
        raise HTTPException(404, "Category not found")
    return category


@router.post("/", response_model=schemas.CategoryResponse, status_code=201)
def create_category(data: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db, data.title)


@router.put("/{category_id}", response_model=schemas.CategoryResponse)
def update_category(category_id: int, data: schemas.CategoryUpdate, db: Session = Depends(get_db)):
    category = crud.update_category(db, category_id, data.title)
    if not category:
        raise HTTPException(404, "Category not found")
    return category


@router.delete("/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db)):
    category = crud.delete_category(db, category_id)
    if not category:
        raise HTTPException(404, "Category not found")
    return {"message": "Category deleted"}