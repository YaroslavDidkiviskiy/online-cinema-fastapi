from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.db.base import Base


class Certification(Base):
	__tablename__ = "certifications"
	
	id = Column(Integer, primary_key=True, index=True)
	name = Column(String(100), unique=True, nullable=False)
	
	movies = relationship("Movie", back_populates="certification")
