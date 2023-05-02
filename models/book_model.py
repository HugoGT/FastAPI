# Book model

from pydantic import BaseModel
from typing import Optional


class BookModel(BaseModel):

    id: Optional[int]
    title: str
    subtitle: Optional[str]
    authors: Optional[str]
    categories: Optional[str]
    published_year: Optional[int]
    average_rating: Optional[float]
    num_pages: Optional[int]
    ratings_count: Optional[int]
