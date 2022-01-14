from app.database import Base
from sqlalchemy import Column, Integer, String, Float, ARRAY, JSON


class Services(Base):
    __tablename__ = 'services'
#     __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    description = Column(String)
    groups = Column(ARRAY(JSON))

    def __repr__(self):
        return f"({self.id}, {self.description}, {self.groups})"
