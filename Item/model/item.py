from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import DB_Base

class UserTable(DB_Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True, index=True, autoincrement=True) 
    name = Column(String, index=True)

    items = relationship("ItemTable", back_populates="user")

class ItemTable(DB_Base):
    __tablename__ = 'item'
    item_id = Column(Integer, primary_key=True, index=True, autoincrement=True) 
    iname = Column(String, index=True)
    user_id = Column(Integer, ForeignKey("user.user_id", ondelete='SET NULL'))

    user = relationship("UserTable", back_populates="items")
