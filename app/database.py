from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database URL (replace with your actual database URL)
DATABASE_URL = "postgresql://postgres:docker@localhost/tenantdb"  # Example for SQLite
# For other databases like PostgreSQL, the URL might look like:
# DATABASE_URL = "postgresql://user:password@localhost/dbname"


engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
