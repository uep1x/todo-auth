from app.models.models import ItemsORM, UsersORM
from app.schemas.schemas import ItemsSchema, UsersSchema


def orm_to_model_auth(orm: UsersORM) -> UsersSchema:
    return UsersSchema(uid=orm.uid, nickname=orm.nickname, password=orm.password, access_cookies=orm.access_cookies)

def orm_to_model_item(orm: ItemsORM) -> ItemsSchema:
    return ItemsSchema(access_cookies=orm.access_cookies, items=orm.items)
