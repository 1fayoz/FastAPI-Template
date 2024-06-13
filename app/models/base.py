from sqlalchemy import Column, Integer, DateTime, func, String
from app.db.base import Base


class BaseModel(Base):
    __abstract__ = True

    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())


class User(BaseModel):
    name = Column(String, unique=True, nullable=False)
