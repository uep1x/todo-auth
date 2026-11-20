# import's
from app.models.models import ItemsORM
from sqlalchemy import any_, func, select, update
from sqlalchemy.orm import Session


# crud's
# get items
def get_items_from_uid(db: Session, uid: str) -> ItemsORM | None:
    items = db.scalars(select(ItemsORM)).all()
    for item in items:
        if item.uid == uid:
            return item
    return None
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
# update filed items
def add_new_access_cookie_in_items(db: Session, user: ItemsORM, new_access_cookie: str):
    db.execute(update(ItemsORM).where(ItemsORM.uid == user.uid).values(access_cookies=func.array_append(ItemsORM.access_cookies, new_access_cookie)))
    db.commit()
# delete field items
def delete_access_cookie_in_items(db: Session, user: ItemsORM, old_access_cookie: str):
    db.execute(update(ItemsORM).where(ItemsORM.uid == user.uid).values(access_cookies=func.array_remove(ItemsORM.access_cookies, old_access_cookie)))
    db.commit()
