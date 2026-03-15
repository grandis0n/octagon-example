from app.db.db import engine, SessionLocal, Base
from app.db import models, crud


def init():
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    category1 = crud.create_category(db, "Programming")
    category2 = crud.create_category(db, "Databases")

    crud.create_book(
        db,
        title="Clean Code",
        description="Guide to writing clean code",
        price=30.5,
        category_id=category1.id
    )

    crud.create_book(
        db,
        title="Fluent Python",
        description="Advanced Python book",
        price=45.0,
        category_id=category1.id
    )

    crud.create_book(
        db,
        title="PostgreSQL Guide",
        description="Learn PostgreSQL",
        price=25.0,
        category_id=category2.id
    )

    crud.create_book(
        db,
        title="SQL Cookbook",
        description="Collection of SQL recipes",
        price=28.0,
        category_id=category2.id
    )

    db.close()
    print("Database initialized!")


if __name__ == "__main__":
    init()