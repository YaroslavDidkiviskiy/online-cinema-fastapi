from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime



class MovieBase(BaseModel):
    name: str
    year: int
    time: int
    imdb: float
    votes: int
    description: str
    certification_id: int
    
class MovieCreate(MovieBase):
    meta_score: Optional[float] = None
    gross: Optional[float] = None
    price: Optional[float] = None
    genres: List[int] = []
    stars: List[int] = []
    directors: List[int] = []


class Movie(MovieBase):
	id: int
	uuid: str
	meta_score: Optional[float]
	gross: Optional[float]
	price: Optional[float]
	
	class Config:
		orm_mode = True
