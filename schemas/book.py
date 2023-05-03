# Book model

from typing import Optional
from pydantic import BaseModel


class Book(BaseModel):
    id: Optional[int]
    title: str
    subtitle: Optional[str]
    authors: Optional[str]
    categories: Optional[str]
    published_year: Optional[int]
    average_rating: Optional[float]
    num_pages: Optional[int]
    ratings_count: Optional[int]