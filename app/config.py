from typing import Any, Dict, Optional

from pydantic import BaseSettings, validator

class Settings(BaseSettings):
    APPDB_HOST: str
    APPDB_USER: str
    APPDB_PASSWORD: str
    APPDB_DATABASE: str

    SQLALCHEMY_DATABASE_URI: Optional[str] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        user=values.get("APPDB_USER")
        password=values.get("APPDB_PASSWORD")
        host=values.get("APPDB_HOST")
        database=values.get("APPDB_DATABASE")
        return f'postgresql://{user}:{password}@{host}/{database}'
    
    class Config:
        case_sensitive = True
        env_file = ".env"

    settings = Settings()