from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime

from datetime import datetime

from src.semc.database.database import Base


class Media(Base):

    __tablename__ = "media"

    id = Column(
        Integer,
        primary_key=True
    )

    filename = Column(
        String,
        nullable=False
    )

    filepath = Column(
        String,
        nullable=False
    )

    media_type = Column(
        String,
        nullable=False
    )

    width = Column(
        Integer
    )

    height = Column(
        Integer
    )

    duration = Column(
        Integer
    )

    date_added = Column(
        DateTime,
        default=datetime.utcnow
    )