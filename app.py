from typing import Annotated

from fastapi import Depends, FastAPI
from sqlalchemy.ext.asyncio import AsyncSession

import schemas
from dependencies import create_session
from lifespan import lifespan
from services import (
    create_advertisement,
    delete_advertisement,
    get_advertisement,
    get_advertisements_query_params,
    get_all_advertisements,
    update_advertisement,
)

app = FastAPI(
    title='Advertisement_FastApi',
    description='Приложение для обьявлений',
    version='0.1.0',
    lifespan=lifespan
)

SessionDep = Annotated[AsyncSession, Depends(create_session)]

@app.post("/advertisement", response_model=schemas.AdResponse)
async def create_ad(session: SessionDep, data: schemas.CreateAdRequest):
    return await create_advertisement(session, data)


@app.get("/advertisement", response_model=list[schemas.AdResponse])
async def read_all_ads(
    session: SessionDep,
    title: str | None=None,
    author: str | None=None,
    price_min: float | None=None,
    price_max: float | None=None,
):
    if title or author or price_min is not None or price_max is not None:
        return await get_advertisements_query_params(
            session, title, author, price_min, price_max
        )
    return await get_all_advertisements(session)


@app.get("/advertisement/{ad_id}", response_model=schemas.AdResponse)
async def read_ad(session: SessionDep, ad_id: int):
    return await get_advertisement(session, ad_id)


@app.patch("/advertisement/{ad_id}", response_model=schemas.AdResponse)
async def update_ad(
    session: SessionDep, 
    ad_id: int, 
    data: schemas.UpdateAdRequest):
    return await update_advertisement(session, ad_id, data)


@app.delete("/advertisement/{ad_id}")
async def delete_ad(session: SessionDep, ad_id: int):
    await delete_advertisement(session, ad_id)
    return {"status": "ok"}





