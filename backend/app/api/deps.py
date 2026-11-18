from app.db.session import SessionLocal
from sqlalchemy.orm import Session


async def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
