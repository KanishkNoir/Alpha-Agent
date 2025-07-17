import os
import sqlmodel
from sqlmodel import Session, SQLModel

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError(
        "DATABASE_URL environment variable is not set. "
        "Please add a PostgreSQL database service in Railway and set the DATABASE_URL."
    )

engine = sqlmodel.create_engine(DATABASE_URL)


# database models
def init_db():
    SQLModel.metadata.create_all(engine)
# api routes
def get_session():
    with Session(engine) as session:
        yield session

