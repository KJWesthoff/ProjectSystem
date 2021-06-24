from app.api.db import Base
from sqlalchemy import Column, Integer, String


class Client(Base):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True)
    country = Column(String(50), nullable=False)
    address = Column(String(50), nullable=False, unique=False)
    

