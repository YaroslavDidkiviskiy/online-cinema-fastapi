from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey, UniqueConstraint, DECIMAL
from sqlalchemy.orm import relationship
from src.db.base import Base


class Movie(Base):
	__tablename__ = 'movies'
	
	id = Column(Integer, primary_key=True, index=True)
	uuid = Column(String(36), unique=True, nullable=False)
	name = Column(String(258), nullable=False)
	year = Column(Integer, nullable=False)
	time = Column(Integer, nullable=False)
	imdb = Column(Float, nullable=False)
	votes = Column(Integer, nullable=False)
	meta_score = Column(Float)
	gross = Column(Float)
	description = Column(Text, nullable=False)
	price = Column(DECIMAL, nullable=False)
	certification_id = Column(Integer, ForeignKey("certifications.id"), nullable=False)
	
	certification = relationship("Certification", back_populates="movies")
	genres = relationship("Genre", secondary="movie_genres", back_populates="movies")
	stars = relationship("Star", secondary="movie_stars", back_populates="movies")
	directors = relationship("Director", secondary="movie_directors", back_populates="movies")
	
	__table_args__ = (UniqueConstraint('name', 'year', 'time', name='_movie_uc'),)
