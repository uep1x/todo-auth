# imports
from app.models.models import UsersORM
from sqlalchemy import func, select, update
from sqlalchemy.orm import Session


# crud's
# get user
def get_user_from_nickname(db: Session, nickname: str) -> UsersORM | None:
    users = db.scalars(select(UsersORM)).all()
    for user in users:
        if user.nickname == nickname:
            return user
    return None
def get_user_from_cookie(db: Session, access_cookie: str) -> UsersORM | None:
    users = db.scalars(select(UsersORM)).all()
    for user in users:
        if access_cookie in user.access_cookies:
            return user
    return None
# create user
def create_user(db: Session, user: UsersORM, type_fix: str = "commit"):
    db.add(user)
    if type_fix == "commit":
        db.commit()
    elif type_fix == "flush":
        db.flush()
    else:
        print("FATAL ERROR IN WRITING DB")
# update filed user
def add_new_access_cookie_in_user(db: Session, user: UsersORM, new_access_cookie: str):
    db.execute(update(UsersORM).where(UsersORM.uid == user.uid).values(access_cookies=func.array_append(UsersORM.access_cookies, new_access_cookie)))
    db.commit()
# delete field user
def delete_access_cookie_in_user(db: Session, user: UsersORM, old_access_cookie: str):
    db.execute(update(UsersORM).where(UsersORM.uid == user.uid).values(access_cookies=func.array_remove(UsersORM.access_cookies, old_access_cookie)))
    db.commit()
