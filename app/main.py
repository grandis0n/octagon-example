from app.db.db import SessionLocal
from app.db import crud


def show_data():
    db = SessionLocal()

    categories = crud.get_categories(db)

    for category in categories:
        print(f"\nCategory: {category.title}")

        for book in category.books:
            print(f"  Book: {book.title}")
            print(f"    Description: {book.description}")
            print(f"    Price: {book.price}")
            print(f"    URL: {book.url}")

    db.close()


if __name__ == "__main__":
    show_data()