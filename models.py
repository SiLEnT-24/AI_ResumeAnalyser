from sqlalchemy import Column, Integer, String, Text, foreignKey
from db import Base

class User(Base):
    _tablename_="users"

    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True)
    password = Column(String(100))

class Reports(Base):
    _tablename_ ="reports"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    resume_text = Column(Text)
    result = Column(Text)

    