from typing import List

from typing import Optional
from model.todo import TodoTable
from model.types.todo import Todo
from schemas.todo import *
from db import get_db_session

class TodoService:
    def __init__(self):
        self.todo_model = TodoTable
    
    # 할일 생성
    def createTodo(self, create_time: datetime, title: str, content: str, parent_id: str) -> TodoTable:
        db = get_db_session()
        try:
            todo = TodoTable(create_time=create_time, title=title, content=content, parent_id=parent_id)
            db.add(todo)
            db.commit()
            db.refresh(todo)
            return todo
        except Exception as e:
            db.rollback()
            raise e
        
    # 유저 아이디로 할일 조회
    def getUserTodos(self, parent_id:str) ->GetUserTodos:
        db = get_db_session()
        try:
            todos=db.query(TodoTable).filter(TodoTable.parent_id == parent_id).all()
            return todos
        except Exception as e:
            return e
        
    # 할일 아이디로 할일 조회
    def getTodoById(self, todo_id: int) -> Optional[TodoTable]:
        db = get_db_session()
        try:
            return db.query(TodoTable).filter(TodoTable.todo_id == todo_id).first()
        except Exception as e:
            return e