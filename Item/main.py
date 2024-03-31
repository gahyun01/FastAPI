from fastapi import FastAPI

from schema import *
from apis import router as main_router
from apis.user import router as user_router
from apis.item import router as item_router

# 백엔드 시작점
app = FastAPI()
app.include_router(main_router)
app.include_router(user_router)
app.include_router(item_router)