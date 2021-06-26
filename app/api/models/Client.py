from sqlalchemy.sql.expression import null
from sqlalchemy.sql.schema import ForeignKey
from app.api.db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates

import sqlalchemy.orm as orm


class Country(Base):
    __tablename__ = "countries"
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=True)
    name_2letter = Column(String(2), nullable=True)
    name_3letter = Column(String(3), nullable=True)
    region = Column(String(15), nullable=True)


class Client(Base):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    country = Column(Integer, ForeignKey('countries.id'))
    address = Column(String(50), nullable=False, unique=False)

class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    email = name = Column(String(50), nullable=False)

    @validates('email')
    def validate_email(self, key, email):
    # make sure email address contains @ character
    assert '@' in email
    return email


    


