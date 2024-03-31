from fastapi import APIRouter, HTTPException

from schema import *
from services.user import UserService

router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)

UserService = UserService()

# 유저 생성 라우터
@router.post("")
async def root(name: str):
    user = UserService.createUser(name)
    if not user:
        raise HTTPException(status_code=404, detail="User not created")
    return {"message": "User created successfully"}

# 유저 아이디로 유저 조회 라우터
@router.get("/{user_id}")
async def root(user_id: int):
    users = UserService.getUser(user_id)
    if users is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user": users}

# 유저별 아이템 조회 라우터
@router.get("/{user_id}/{id}/items")
async def root(user_id: int) -> GetAllItemOutput:
    items = UserService.getUserItem(user_id)
    if items is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"items": items}