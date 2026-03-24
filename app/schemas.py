from pydantic import BaseModel


# ========= CATEGORY =========

class CategoryBase(BaseModel):
    title: str


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryBase):
    pass


class CategoryResponse(CategoryBase):
    id: int

    class Config:
        orm_mode = True


# ========= BOOK =========

class BookBase(BaseModel):
    title: str
    description: str | None = None
    price: float | None = None
    url: str | None = ""
    category_id: int


class BookCreate(BookBase):
    pass


class BookUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    price: float | None = None
    url: str | None = None
    category_id: int | None = None


class BookResponse(BookBase):
    id: int

    class Config:
        orm_mode = True