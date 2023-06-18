from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert, update

from src.auth.link import get_async_session
from src.auth.models import User
from src.roles.models import Role
from src.roles.schemas import roles, Rolename

router = APIRouter(
    prefix='/user',
    tags=['USERS']
)


@router.get('/{user_id}')
async def get_user(user_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(User).where(User.id == user_id)
    result = await session.execute(query)
    users = [inf for inf in result.first()]
    return users


@router.patch('/role')
async def role_for_user(user_id: int, new_role: Rolename, session: AsyncSession = Depends(get_async_session)):
    user = await session.get(User, user_id)
    user_role = Role(name=new_role.name, permissions=roles.get(new_role))
    user.role = user_role.name
    await session.commit()
    return user
