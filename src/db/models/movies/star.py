from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.db.base import Base


class Star(Base):
	__tablename__ = 'stars'
	
	id = Column(Integer, primary_key=True, index=True)
	name = Column(String(100), unique=True, nullable=False)
	
	movies = relationship("Movie", secondary="movie_stars", back_populates="stars")
