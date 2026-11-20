# imports
from pydantic import BaseModel as BM


# auth schemas
# UsersSchema
class UsersSchema(BM):
    uid: str
    nickname: str
    password: str
    access_cookies: list[str]
# SignUp
class SignUpSchema(BM):
    nickname: str
    password: str
# LogIn
class LogInSchema(BM):
    nickname: str
    password: str
# LogOut
class LogOutSchema(BM):
    access_cookie: str
# item schemas
# Item ToDo's schema
class ItemsSchema(BM):
    access_cookies: list[str]
    items: list[dict]
class GetItemSchema(BM):
    access_cookie: str
