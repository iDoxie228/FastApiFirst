from db import Session


async def create_session():
    async with Session() as session:
        yield session

