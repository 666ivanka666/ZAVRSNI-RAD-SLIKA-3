import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    pin = db.Column(db.String, unique=True, nullable=False)
    admin = db.Column(db.Boolean, default=0, nullable=False)
    active = db.Column(db.Boolean, default=1, nullable=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"