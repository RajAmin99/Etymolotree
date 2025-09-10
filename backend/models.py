from sqlalchemy import Column, Integer, String
from .database import Base

class Word(Base):
    __tablename__ = "words"

    id = Column(Integer, primary_key=True, index=True)
    word = Column(String, index=True, nullable=False)
    language = Column(String)
    origin = Column(String)
    history = Column(String)

