from settings import settings
from sqlalchemy.exc.asyncio import create_async_engine, async_sessionmaker


engine = create_async_engine(settings.DATABASE_URL_ASYNC, echo=True)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

async def get_async_session():
    async with async_session_maker() as session:
        try:
            yield session
        finally:
            await session.close()
