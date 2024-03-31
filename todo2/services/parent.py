from typing import List

from typing import Optional
from model.parent import ParentTable
from model.types.parent import Parent
from schemas.parent import *
from db import get_db_session

class ParentService:
    def __init__(self):
        self.parent_model = ParentTable
    
    # 유저 생성
    def createParent(self, createParentInput: CreateParentInput) -> ParentTable:
        db = get_db_session()
        try:
            parent = ParentTable(parent_id=createParentInput.parent_id,
                                 email=createParentInput.email,
                                 password=createParentInput.password,
                                 name=createParentInput.name)

            db.add(parent)
            db.commit()
            db.refresh(parent)
            return parent
        except Exception as e:
            db.rollback()
            raise e
        
    # 유저 아이디로 유저 조회
    def getParentById(self, parent_id: str) -> ParentTable:
        db = get_db_session()
        try:
            return db.query(ParentTable).filter(ParentTable.parent_id == parent_id).first()
        except Exception as e:
            return e
        
    # 유저 이메일로 유저 조회
    def getParentByemail(self, email:str) -> ParentTable:
        db = get_db_session()
        try:
            return db.query(ParentTable).filter(ParentTable.email == email).first()
        except Exception as e:
            return e
        
    # 유저 정보 수정
    def updateParent(self, parent_id:str, updateParentInput: UpdateParentInput) -> Optional[Parent]:
        db = get_db_session()
        try:
            parent = db.query(ParentTable).filter(ParentTable.parent_id == parent_id).first()
            if parent == None:
                return None
            setattr(parent, "email", updateParentInput.email)
            setattr(parent, "password", updateParentInput.password)
            setattr(parent, "name", updateParentInput.name)

            db.add(parent)
            db.commit()
            db.refresh(parent)

            return parent
        except Exception as e:
            db.rollback()
            raise e

    # 유저 삭제
    def deleteParent(self, parent_id: str) -> Optional[Parent]:
        db = get_db_session()
        try:
            parent = db.query(ParentTable).filter(ParentTable.parent_id == parent_id).first()
            if parent == None:
                return None
            
            db.delete(parent)
            db.commit()

            return parent
        except Exception as e:
            db.rollback()
            raise e