from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from models import Advertisement
from sqlalchemy import select

async def create_advertisement(session, data):
    ad = Advertisement(**data.model_dump())
    session.add(ad)
    await session.commit()
    await session.refresh(ad)
    return ad

async def get_advertisement(session, ad_id: int):
    ad = await session.get(Advertisement, ad_id)
    if not ad:
        raise HTTPException(status_code=404, detail='Not found')
    return ad

async def get_all_advertisements(session):
    ad = await session.execute(select(Advertisement))
    return ad.scalars().all()

async def get_advertisements_query_params(session,
        title: str | None=None,
        author: str | None=None,
        price_min: float | None=None,
        price_max: float | None=None,
):
    query = select(Advertisement)
    if title:
        query = query.where(Advertisement.title.ilike(f'%{title}%'))
    if author:
        query = query.where(Advertisement.author.ilike(f'%{author}%'))
    if price_min is not None:
        query = query.where(Advertisement.price >= price_min)
    if price_max is not None:
        query = query.where(Advertisement.price <= price_max)
    result = await session.execute(query)
    return result.scalars().all()


async def update_advertisement(session, ad_id, data):
    ad = await get_advertisement(session, ad_id)
    for key, value in data.model_dump(exclude_none=True).items():
        setattr(ad, key, value)
    await session.commit()
    await session.refresh(ad)
    return ad

async def delete_advertisement(session, ad_id):
    ad = await get_advertisement(session, ad_id)
    await session.delete(ad)
    await session.commit()
