from uuid import uuid4

from app.api.deps import get_db
from app.crud.item import (
    add_new_access_cookie_in_items,
    create_items,
    delete_access_cookie_in_items,
    get_items_from_uid,
)
from app.crud.user import (
    add_new_access_cookie_in_user,
    create_user,
    delete_access_cookie_in_user,
    get_user_from_cookie,
    get_user_from_nickname,
)
from app.models.models import ItemsORM, UsersORM
from app.schemas.mappers import orm_to_model_auth
from app.schemas.schemas import LogInSchema, LogOutSchema, SignUpSchema
from app.services.crypt import decrypt, encrypt
from app.services.generation_cookie import generation_cookie
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.status import HTTP_401_UNAUTHORIZED, HTTP_403_FORBIDDEN

router = APIRouter()

@router.post("/signup")
def signup(payload: SignUpSchema, db: Session = Depends(get_db)) -> dict:
    if get_user_from_nickname(db, payload.nickname) is None:
        uid = str(uuid4())
        access_cookie = generation_cookie(uid, payload.nickname)
        new_user = UsersORM(uid=uid, nickname=payload.nickname, password=encrypt(payload.password), access_cookies=[access_cookie])
        new_items = ItemsORM(uid=uid, access_cookies=[access_cookie], items=[])
        create_user(db, new_user, "flush")
        create_items(db, new_items)
        return {"User": orm_to_model_auth(new_user), "NewAccessCookie": access_cookie}
    else:
        raise HTTPException(status_code=HTTP_403_FORBIDDEN)

@router.post("/login")
def login(payload: LogInSchema, db: Session = Depends(get_db)) -> dict:
    if (user := get_user_from_nickname(db, payload.nickname)) is not None and user.nickname == payload.nickname and (items := get_items_from_uid(db, user.uid)) is not None:
        if decrypt(user.password) == payload.password:
            access_cookie = generation_cookie(user.uid, user.nickname, False)
            add_new_access_cookie_in_user(db, user, access_cookie)
            add_new_access_cookie_in_items(db, items, access_cookie)
            return {"User": orm_to_model_auth(user), "NewAccessCookie": access_cookie}
        else:
            raise HTTPException(status_code=HTTP_403_FORBIDDEN)
    else:
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED)

@router.post("/logout")
def logout(payload: LogOutSchema, db: Session = Depends(get_db)) -> dict:
    if (user := get_user_from_cookie(db, payload.access_cookie)) is not None and (items := get_items_from_uid(db, user.uid)) is not None:
        delete_access_cookie_in_user(db, user, payload.access_cookie)
        delete_access_cookie_in_items(db, items, payload.access_cookie)
        return {"DeletedAccessCookie": payload.access_cookie}
    else:
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED)
