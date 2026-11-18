from contextlib import asynccontextmanager

from app.api import api
from app.db.session import engine
from app.models.models import Base
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(_: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(redoc_url=None, docs_url="/sf", lifespan=lifespan)

app.include_router(api.router, prefix="/api")
