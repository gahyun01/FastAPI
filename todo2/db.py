from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from core.env import Env


DB_Base = declarative_base()
def create_db_sessionLocal():
    env = Env()
    DB_URL = f'mysql+pymysql://{env.get("MYSQL_USER")}:{env.get("MYSQL_PASSWORD")}@{env.get("MYSQL_HOST")}:{env.get("MYSQL_PORT")}/{env.get("MYSQL_DATABASE")}'

    engine = create_engine(DB_URL)

    return sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 세션을 생성하는 함수를 호출하여 세션을 생성한다.
SessionLocal = create_db_sessionLocal()


# 이 함수를 통해 데이터베이스와 연결할 수 있다.
def get_db_session():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()