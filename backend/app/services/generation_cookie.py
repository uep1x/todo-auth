from datetime import datetime

from app.services.crypt import encrypt


def generation_cookie(uid: str, nickname: str, admin_status: bool = False) -> str:
    date_login = datetime.now()
    return encrypt(f"{uid}.{nickname}.{date_login}.{admin_status}.%$#^@*!")
