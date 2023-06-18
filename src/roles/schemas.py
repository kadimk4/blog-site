from typing import Optional

from pydantic import BaseModel
from enum import Enum

roles = {
    'user': ['see', 'post'],
    'advanced': ['see', 'post', 'comment'],
    'moderator': ['see', 'post', 'comment', 'delete', 'ban'],
    'administrator': ['all permissions']
}


class Rolename(Enum):
    user = 'user'
    advanced = 'advanced'
    moderator = 'moderator'
    administrator = 'administrator'


class Role(BaseModel):
    id: int
    owner_id: int
    name: Optional[Rolename]
    date_added: Optional[str]
    permissions: str
