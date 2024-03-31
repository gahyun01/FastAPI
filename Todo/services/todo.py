from typing import List, Optional

from model import TodoTable
from schema import *
from db import get_db_session

class TodoService:
    def __init__(self):
        self.model = Todo

    def _getTodoById(self, todo_id: int) -> Optional[Todo]:
        try:
            db = get_db_session()
            return db.query(TodoTable).filter(TodoTable.id == todo_id).first()
        except Exception as e:
            return None

    def getAll(self) -> List[TodoTable]:
        db = get_db_session()
        try:
            return db.query(TodoTable).all()
        except Exception as e:
            return []
        
    def getOne(self, todo_id: int) -> Optional[TodoTable]:   # Optional은 TodoTable가 들어 올 수도 안들어올 수도 았음.
        return self._getTodoById(todo_id)
    
    def createOne(self, todo: str):
        db = get_db_session()
        try:
            new_todo = TodoTable(todo=todo)
            db.add(new_todo) # 인스턴스 추가
            db.commit() # table객체 저장
            db.refresh(new_todo) # db에 적용

            return new_todo
        except Exception as e:
            db.rollback()
            raise Exception("Todo create failed")
    
    def putOne(self, todo_id: int, update_todo: str) -> Optional[Todo]:
        db = get_db_session()
        try:
            todo = db.query(TodoTable).filter(TodoTable.id == todo_id).first()
            if todo == None:
                return None
            
            # todo.todo = update_todo <- 이렇게 하면 반복문 안됨
            setattr(todo, "todo", update_todo)  # setatter 장점 : 반복문을 돌릴 수 있음 ( todo_id행의 "todo" key를 update_todo로 변경 )

            db.add(todo)
            db.commit()
            db.refresh(todo)
            return todo

        except Exception as e:
            db.rollback()
            raise Exception("Todo put failed")
    
    def delOne(self, todo_id: int) -> bool:
        db = get_db_session()
        try:
            todo = db.query(TodoTable).filter(TodoTable.id == todo_id).first()
            if todo == None:
                return False
            
            db.delete(todo)
            db.commit()
            
            return True
        
        except Exception as e:
            db.rollback()
            raise Exception("Todo delete failed")