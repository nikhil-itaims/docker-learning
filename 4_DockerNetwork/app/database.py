from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()
import os

DB_URL = os.getenv("DB_URL")

try:
    engine = create_engine(DB_URL, echo=True)
except Exception as e:
    print(str(e))

SessionLocal = sessionmaker(autocommit=False,autoflush=False, bind=engine)

Base = declarative_base()
