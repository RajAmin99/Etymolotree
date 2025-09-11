from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class Word(Base):
    __tablename__ = "words"

    id = Column(Integer, primary_key=True, index=True)
    word = Column(String, index=True, nullable=False)
    language = Column(String)
    origin = Column(String)
    history = Column(String)

"""
class Etymology(Base):
    __tablename__ = "etymologies"

    id = Column(Integer, primary_key=True, index=True)
    word_id = Column(Integer, ForeignKey("words.id"), nullable=False)
    etymology = Column(String, nullable=False)

    word = relationship("Word", back_populates="etymologies")
"""