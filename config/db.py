from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model.user import Base

DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/pyserver"

engine = create_engine(DATABASE_URL)

Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()