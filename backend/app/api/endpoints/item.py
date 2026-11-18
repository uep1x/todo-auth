from app.api.deps import get_db
from app.crud.item import get_items_from_cookie
from app.schemas.mappers import orm_to_model_item
from app.schemas.schemas import GetItemSchema
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.status import HTTP_404_NOT_FOUND

router = APIRouter()

@router.post("/get-items")
def get_items(payload: GetItemSchema, db: Session = Depends(get_db)) -> dict:
    if (items := get_items_from_cookie(db, payload.access_cookie)) is not None:
        return {"items": orm_to_model_item(items)}
    else:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND)
