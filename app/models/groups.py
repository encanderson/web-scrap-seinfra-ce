from app.database import Base
from sqlalchemy import Column, Integer, String, Float, ARRAY, JSON


class Groups(Base):
    __tablename__ = 'groups'
#     __table_args__ = {'extend_existing': True}

    id = Column(String, primary_key=True)
    description = Column(String)
    compositions = Column(ARRAY(JSON))

    def __repr__(self):
        return f"({self.id}, {self.description}, {self.compositions})"
