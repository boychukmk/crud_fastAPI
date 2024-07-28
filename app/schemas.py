from pydantic import BaseModel
from typing import List, Optional

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    pass

class UserInGroup(UserBase):
    id: int

    class Config:
        orm_mode = True

class GroupBase(BaseModel):
    name: str

class GroupCreate(GroupBase):
    user_ids: Optional[List[int]] = []

class GroupInUser(GroupBase):
    id: int

    class Config:
        orm_mode = True

class User(UserBase):
    id: int
    groups: List[GroupInUser] = []

    class Config:
        orm_mode = True

class Group(GroupBase):
    id: int
    users: List[UserInGroup] = []

    class Config:
        orm_mode = True
