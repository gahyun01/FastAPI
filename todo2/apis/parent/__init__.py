from fastapi import APIRouter, HTTPException
from fastapi import Depends

from typing import Optional
from schemas.parent import *
from services.parent import ParentService

from auth.auth_bearer import JWTBearer
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from auth.auth_handler import signJWT

router = APIRouter(
    prefix="/parent",
    tags=["parent"],
    responses={404: {"description": "Not found"}},
)

parentService = ParentService()

# 유저 생성
@router.post("")
async def createParesnt(createParentInput: CreateParentInput):
    parent = parentService.createParent(createParentInput)
    # return{
    #     "success": True if parent else False,
    #     "parent": parent
    # }
    return JSONResponse(status_code=201, content={
        'parent': jsonable_encoder(parent),
        'x-jwt': signJWT(parent.parent_id)
    })

# 유저 아이디로 유저 조회
@router.get("/")
async def getParentById(uid: str) -> Optional[GetParentById]:
    #parent_id = GetParentById.parent_id
    parent = parentService.getParentById(uid)
    if not parent:
        raise HTTPException(status_code=404, detail="User not found")
    return parent

# 유저 이메일로 유저 조회
@router.get("/{email}")
async def getParentByemail(email: str) -> Optional[GetParentByEmail]:
    parent = parentService.getParentByemail(email)
    if not parent:
        raise HTTPException(status_code=404, detail="User not found")
    return parent

# 유저 수정
@router.put("/", dependencies=[Depends(JWTBearer())])
async def updateParent(UpdateParentInput: UpdateParentInput,
               parent_id:str = Depends(JWTBearer())) -> UpdateParentOutput:
    if UpdateParentInput.parent_id != parent_id:
        raise HTTPException(status_code=403, detail="Forbidden")
    parent = parentService.updateParent(parent_id, UpdateParentInput)
    if parent is None:
        raise HTTPException(status_code=404, detail="User not found")
    return{
        "success": True if parent else False,
        "parent": parent
    }

# 유저 삭제
@router.delete("/", dependencies=[Depends(JWTBearer())])
async def deleteParent(DeleteParentInput: DeleteParentInput,
                       parent_id:str = Depends(JWTBearer())) -> DeleteParentOutput:
    if DeleteParentInput.parent_id != parent_id:
        raise HTTPException(status_code=403, detail="Forbidden")
    parent = parentService.deleteParent(parent_id)
    if parent is None:
        raise HTTPException(status_code=404, detail="User not found")
    return{
        "success": True if parent else False,
        "parent": parent
    }