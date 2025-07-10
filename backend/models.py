from sqlalchemy import Column, Integer, String
from .database import Base

class Fact(Base):
    __tablename__ = "facts"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String, index=True)
    content = Column(String, index=True)
