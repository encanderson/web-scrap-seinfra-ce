from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


engine = create_engine(
    'sqlite:////home/enganderson/OneDrive/seinfra-ce/database.db')


Session = sessionmaker(bind=engine)

session = Session()

Base = declarative_base()
