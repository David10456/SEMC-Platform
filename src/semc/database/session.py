from sqlalchemy.orm import sessionmaker

from src.semc.database.database import engine


SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)


def get_session():

    session = SessionLocal()

    try:
        return session

    finally:
        session.close()