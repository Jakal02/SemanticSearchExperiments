import datetime

from pydantic import BaseModel, validator, field_validator, PositiveInt
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, UniqueConstraint

from frage.database import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    date_created = Column(DateTime, default=datetime.datetime.utcnow())
    date_modified = Column(DateTime, default=datetime.datetime.utcnow())

    title = Column(String)
    body = Column(String)


class PostCreate(BaseModel):
    title: str
    body: str


class PostRetrieve(BaseModel):
    title: str
    body: str
    date_created: datetime.datetime
    date_modified: datetime.datetime
    id: PositiveInt

    model_config = {
        "from_attributes": True,
    }
