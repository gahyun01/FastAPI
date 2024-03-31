from fastapi import APIRouter, HTTPException

from schema import *
from services.todo import TodoService

router = APIRouter(
    prefix="/todo",
    tags=["todo"],
    responses={404: {"description": "Not found"}},
)

todoService = TodoService()

@router.post("/create")
async def root(todo: str):
    print(f"Todo: {todo}")
    todos = todoService.createOne(todo)
    if not todos:
        raise HTTPException(status_code=400, detail="Todo not created")
    return {"message": "Todo created successfully"}

@router.get("/")
async def root() -> GetAllTodoOutput:
    todos = todoService.getAll()
    return {"todos": todos}

@router.get("/{todo_id}")
async def root(todo_id: int):
    todos = todoService.getOne(todo_id)
    if todos is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"todo": todos}

@router.put("/{todo_id}")
async def root(todo_id: int, update_todo: str):
    todo = todoService.putOne(todo_id, update_todo)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Todo updated successfully"}

@router.delete("/{todo_id}")
async def root(todo_id: int):
    todo = todoService.delOne(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Todo deleted successfully"}