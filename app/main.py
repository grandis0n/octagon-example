from fastapi import FastAPI

from app.api import books, categories

app = FastAPI(title="Books API")


@app.get("/health")
def health():
    return {"status": "ok"}


app.include_router(categories.router)
app.include_router(books.router)