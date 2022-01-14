from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.config import settings


engine = create_engine(settings.POSTGRESQL_URI)


Session = sessionmaker(bind=engine)

session = Session()

Base = declarative_base()
