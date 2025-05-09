from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from applications.users.schemas import BaseFields, RegisterUserFields

from database.session_dependencies import get_async_session

router_users = APIRouter()


@router_users.post("/create", status_code=status.HTTP_201_CREATED)
async def creat_user(new_user: RegisterUserFields, session: AsyncSession = get_async_session()) -> BaseFields:
    print(session)
    return new_user
