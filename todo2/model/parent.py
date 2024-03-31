from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from db import DB_Base

# +-----------+--------------+------+-----+---------+-------+
# | Field     | Type         | Null | Key | Default | Extra |
# +-----------+--------------+------+-----+---------+-------+
# | parent_id | varchar(255) | NO   | PRI | NULL    |       |
# | email     | varchar(255) | NO   |     | NULL    |       |
# | password  | varchar(255) | NO   |     | NULL    |       |
# | name      | varchar(50)  | NO   |     | NULL    |       |
# +-----------+--------------+------+-----+---------+-------+

class ParentTable(DB_Base):
    __tablename__ = 'parent'

    parent_id = Column(String, primary_key=True, index=True)
    email = Column(String, index=True)
    password = Column(String, index=True)
    name = Column(String, index=True)

    # 자식 테이블과 관계를 맺는다.
    todos = relationship("TodoTable", back_populates="parent")