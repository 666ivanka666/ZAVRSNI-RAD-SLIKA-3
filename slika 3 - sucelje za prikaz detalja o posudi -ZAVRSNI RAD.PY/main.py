import sqlalchemy as db
from sqlalchemy.orm import sessionmaker

from database import Base

db_name = "PyPosuda.db"
db_engine = db.create_engine(f"sqlite:///{db_name}")
Base.metadata.create_all(db_engine, checkfirst=True)

Session = sessionmaker()
Session.configure(bind=db_engine)

session = Session()
