from fastapi import APIRouter, HTTPException

from schema import *
from services.item import ItemService

router = APIRouter(
    prefix="/item",
    tags=["item"],
    responses={404: {"description": "Not found"}},
)

ItemService = ItemService()

# 아이템 생성 라우터
@router.post("/{user_id}")
async def root(iname: str, user_id: int):
    items = ItemService.createItem(iname, user_id)
    if not items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item created successfully"}

# 모든 아이템 조회 라우터
@router.get("s")
async def root() -> GetAllItemOutput:
    items = ItemService.getAllItem()
    return {"items": items}

# 아이템 업데이트 라우터
@router.put("/{user_id}/{id}")
async def root(id: int, newname: str):
    items = ItemService. updateItem(id, newname)
    if items is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item updated successfully"}

# 아이템 삭제 라우터
@router.delete("/{user_id}/{id}")
async def root(id: int):
    items = ItemService.deleteItem(id)
    if items is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted successfully"}