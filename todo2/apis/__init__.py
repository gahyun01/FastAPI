# apis / __init__.py
from fastapi import APIRouter
    
router = APIRouter(
    prefix="",
    tags=[""],
    responses={404: {"description": "Not found"}},
)
@router.get("/")
async def root():
    return "Hello, World!"