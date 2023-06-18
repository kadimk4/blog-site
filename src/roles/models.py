from datetime import datetime

from sqlalchemy.orm import declarative_base

from src.auth.models import User
from sqlalchemy import Column, Integer, String, MetaData, Table, ForeignKey, TIMESTAMP

Base = declarative_base()


class Role(Base):
    __tablename__ = 'roles'
    id = Column(String, primary_key=True)
    owner_id = Column(Integer, ForeignKey(User.id))
    name = Column(String)
    date_added = Column(TIMESTAMP, default=datetime.utcnow)
    permissions = Column(String)


metadata = Base.metadata
