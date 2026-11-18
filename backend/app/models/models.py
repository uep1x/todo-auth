# imports
from sqlalchemy import ARRAY, ForeignKey, String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


# models
# Base Model
class Base(DeclarativeBase):
    pass
# DB Model
class UsersORM(Base):
    __tablename__ = "users_db"

    uid: Mapped[str] = mapped_column(primary_key=True)
    nickname: Mapped[str]
    password: Mapped[str]
    access_cookies: Mapped[list[str]] = mapped_column(ARRAY(String))
# Item model
class ItemsORM(Base):
    __tablename__ = "items_db"

    uid: Mapped[str] = mapped_column(ForeignKey("users_db.uid", ondelete="CASCADE"), primary_key=True)
    access_cookies: Mapped[list[str]] = mapped_column(ARRAY(String))
    items: Mapped[list[dict]] = mapped_column(JSONB, default=list)
