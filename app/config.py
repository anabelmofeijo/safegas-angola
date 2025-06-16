from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "SafeGas Angola"
    VERSION: str = "2.0"
    
    # MongoDB
    MONGODB_URI: str = "mongodb://localhost:27017"
    MONGODB_DB_NAME: str = "safegas"

    # JWT
    SECRET_KEY: str = "supersecreta"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # CORS
    ALLOWED_ORIGINS: list[str] = ["*"]

    class Config:
        env_file = ".env"

settings = Settings()
