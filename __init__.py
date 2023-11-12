from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base 
from utils import get_environment_variable

DATABASE_URL = get_environment_variable("DATABASE_URL", "sqlite:///./test.db")

db_engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)

Base = declarative_base()