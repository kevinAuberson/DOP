from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

postgres_user = getenv("POSTGRES_USER")
postgres_password = getenv("POSTGRES_PASSWORD")
postgres_host = getenv("POSTGRES_HOST")
postgres_db = getenv("POSTGRES_DB")
DATABASE_URL = (
    f"postgresql://{postgres_user}:{postgres_password}@{postgres_host}/{postgres_db}"
)

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()