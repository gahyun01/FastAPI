from fastapi import FastAPI
from typing import List, Optional

from model.types.todo import Todo
from schema import *
from apis import router as main_router
from apis.todo import router as todo_router

# 백엔드 시작점
app = FastAPI()
app.include_router(main_router)
app.include_router(todo_router)