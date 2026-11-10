from sqlalchemy import Column, String, Integer, Float, Date, Text
from sqlalchemy.orm import DeclarativeBase
from datetime import datetime


class Base(DeclarativeBase):
    pass

class Advertisement(Base):
    __tablename__ = 'advertisement'
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    price = Column(Float, nullable=False)
    author = Column(String(200), nullable=False)
    created_at = Column(Date, default=datetime.now, nullable=False)