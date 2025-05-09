from settings import settings
from sqlalchemy.exc.asyncio import create_async_engine


engine = create_async_engine(settings.DATABASE_URL_ASYNC, echo=True)