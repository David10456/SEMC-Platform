from src.semc.database.database import Base
from src.semc.database.database import engine

import src.semc.database.models

print("Creating database tables...")

Base.metadata.create_all(bind=engine)

print("Done!")