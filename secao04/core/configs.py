from typing import List

from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    '''
    Configurações gerais usadas na aplicação
    '''
    API_V1_str  = '/api/v1'
    DB_URL  = "postgresql+asyncpg://localhost:5432/db?user=geek&password=university"
    DBBaseModel = declarative_base()

    class Config: 
        case_sensitive = True

settings = Settings()

