# imports
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

# url at the db, creating engine and create Sessions
DATABASE_URL = f"postgresql+psycopg://postgres:{os.getenv('PASSWORD_DB')}@127.0.0.1:8787/postgres"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
