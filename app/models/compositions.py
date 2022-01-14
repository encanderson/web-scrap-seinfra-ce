from app.database import Base
from sqlalchemy import Column, Integer, String, Float, ARRAY, JSON


class Compositions(Base):
    __tablename__ = 'compositions'
#     __table_args__ = {'extend_existing': True}

    id = Column(String, primary_key=True)
    description = Column(String)
    unid = Column(String)
    price = Column(Float)
    insumos = Column(ARRAY(JSON))

    def __repr__(self):
        return f"({self.id}, {self.description}, {self.unid}, {self.price}, {self.insumos})"
