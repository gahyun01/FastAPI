from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db import DB_Base

# +-------------+-------------+------+-----+---------+----------------+
# | Field       | Type        | Null | Key | Default | Extra          |
# +-------------+-------------+------+-----+---------+----------------+
# | todo_id     | int(11)     | NO   | PRI | NULL    | auto_increment |
# | create_time | datetime    | NO   |     | NULL    |                |
# | title       | varchar(50) | NO   |     | NULL    |                |
# | content     | text        | YES  |     | NULL    |                |
# | parent_id   | varchar(255)| YES  | MUL | NULL    |                |
# +-------------+-------------+------+-----+---------+----------------+

class TodoTable(DB_Base):
    __tablename__ = 'todo'

    todo_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    create_time = Column(DateTime, index=True)
    title = Column(String, index=True)
    content = Column(String, index=True)
    parent_id = Column(String, ForeignKey('parent.parent_id'))

    # 부모 테이블과 관계를 맺는다.
    parent = relationship("ParentTable", back_populates="todos")