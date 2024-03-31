from fastapi import APIRouter, HTTPException
from fastapi import Depends

from typing import Optional
from schemas.todo import *
from services.todo import TodoService
from auth.auth_bearer import JWTBearer

router = APIRouter(
    prefix="/todo",
    tags=["todo"],
    responses={404: {"description": "Not found"}},
)

todoService = TodoService()

# 할일 생성
@router.post("")
async def createTodo(createTodoInput : CreateTodoInput,
                     parent_id:str = Depends(JWTBearer())) -> CreateTodoOutput:
    create_time = createTodoInput.create_time
    title = createTodoInput.title
    content = createTodoInput.content
    if not create_time or not title or not content:
        raise HTTPException(status_code=400, detail="create_time, title, content is required")
    todo = todoService.createTodo(create_time, title, content, parent_id)
    return{
        "success": True if todo else False,
        "todo": todo
    }

# 유저 아이디로 할일 조회
@router.get("/",  dependencies=[Depends(JWTBearer())])
async def getUserTodos(parent_id:str = Depends(JWTBearer())) -> GetUserTodos:
    todos = todoService.getUserTodos(parent_id)
    if not todos:
        raise HTTPException(status_code=404, detail="Todos not found")
    return {"todos":todos}

# 할일 아이디로 할일 조회
@router.get("/{todo_id}")
async def getTodoById(todo_id: int) -> Optional[GetTodoById]:
    todo = todoService.getTodoById(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo