# import's
from app.models.models import ItemsORM
from sqlalchemy import any_, select
from sqlalchemy.orm import Session


# crud's
# get items
def get_items_from_cookie(db: Session, access_cookie: str) -> ItemsORM | None:
    items = db.scalar(select(ItemsORM).where(any_(ItemsORM.access_cookies) == access_cookie))
    if items:
        return items
# create items
def create_items(db: Session, items: ItemsORM, type_fix: str = "commit"):
    db.add(items)
    if type_fix == "commit":
        db.commit()
    elif type_fix == "flush":
        db.flush()
    else:
        print("FATAL ERROR IN WRITING DB")
