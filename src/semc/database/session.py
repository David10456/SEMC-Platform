from sqlalchemy.orm import sessionmaker

from src.semc.database.database import engine

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)