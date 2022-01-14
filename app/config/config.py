from pydantic import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()


class Settings(BaseSettings):
    POSTGRESQL_URI: str = os.getenv("POSTGRESQL_URI")
    PATH_FOLDER: str = os.getenv("PATH_FOLDER")

    class Config:
        case_sensitive = True


settings = Settings()
