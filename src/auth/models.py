from sqlalchemy import Column, Integer, String, MetaData, Table, TIMESTAMP
from datetime import datetime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    role = Column(String)
    hashed_password = Column(String)
    reg_at = Column(TIMESTAMP, default=datetime.utcnow)


metadata = Base.metadata
