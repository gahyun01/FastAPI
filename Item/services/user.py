from typing import List

from model.item import UserTable, ItemTable
from schema import *
from db import get_db_session

class UserService:
    def __init__(self):
        self.user_model = user

    # 유저 생성
    def createUser(self, name: str):
        db = get_db_session()
        try:
            # try에 들어오지만 error 발생
            new_user = UserTable(name=name)
            db.add(new_user)
            db.commit()
            db.refresh(new_user)

            return new_user
        except Exception as e:
            db.rollback()
            raise Exception("User create failed")
        
    # 유저 아이디로 유저 조회
    def getUser(self, user_id: int):
        print(f"user_id: {user_id}")
        db = get_db_session()
        try:
            return db.query(UserTable).filter(UserTable.user_id == user_id).first()
        except Exception as e:
            return None
        
    # 유저별 아이템 조회
    def getUserItem(self, user_id: int) -> List[ItemTable]:
        db = get_db_session()
        try:
            return db.query(ItemTable).filter(ItemTable.user_id == user_id).all()
        except Exception as e:
            return []