import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Use environment variable for production (Render)
# Falls back to SQLite for local development
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./sql_app.db")

# For Render PostgreSQL, the URL looks like:
# postgres://user:pass@host:port/dbname

# Configure engine based on database type
if DATABASE_URL.startswith("postgres"):
    engine = create_engine(
        DATABASE_URL,
        connect_args={"options": "-c timezone=utc"}  # Critical for PostgreSQL
    )
else:
    # SQLite configuration
    engine = create_engine(
        DATABASE_URL,
        connect_args={"check_same_thread": False}  # Required for SQLite
    )

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
