from typing import List, Optional

from model.item import ItemTable
from schema import *
from db import get_db_session

class ItemService:
    def __init__(self):
        self.item_model = item

    # 아이템 생성
    def createItem(self, iname: str, user_id: int):
        db = get_db_session()
        try:
            new_item = ItemTable(iname = iname, user_id = user_id)
            db.add(new_item)
            db.commit()
            db.refresh(new_item)

            return new_item
        except Exception as e:
            db.rollback()
            raise Exception("Item create faild")
        
    # 모든 아이템 조회
    def     getAllItem(self) -> List[ItemTable]:
        db = get_db_session()
        try:
            return db.query(ItemTable).all()
        except Exception as e:
            print("ASDASDASD")
            print(e)
            return []
        
    # 아이템 업데이트
    def updateItem(self, id: int, newname: str) -> Optional[item]:
        db = get_db_session()
        try:
            items = db.query(ItemTable).filter(ItemTable.item_id == id).first()
            if items == None:
                return None
            
            setattr(items, "iname", newname) # setattr(dict, key, value)

            db.add(items)
            db.commit()
            db.refresh(items)
            return items
        
        except Exception as e:
            db.rollback()
            raise Exception("Item put failed")
        
    # 아이템 삭제
    def deleteItem(self, id: int) -> bool:
        db = get_db_session()
        try:
            items = db.query(ItemTable).filter(ItemTable.item_id == id).first()
            if items == None:
                return False
            
            db.delete(items)
            db.commit()

            return True
        
        except Exception as e:
            db.rollback()
            raise Exception("Item delete failed")