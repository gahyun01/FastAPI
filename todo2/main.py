from fastapi import FastAPI

from schemas import *
from apis import router as main_router
from apis.parent import router as parent_router
from apis.todo import router as todo_router

# 백엔드 시작점
app = FastAPI()
app.include_router(main_router)
app.include_router(parent_router)
app.include_router(todo_router)