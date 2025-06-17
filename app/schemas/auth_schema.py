from app import BaseModel, datetime
from app import EmailStr


class AuthRegister(BaseModel):
    id: int
    name: str
    email: EmailStr
    password: str
    datetime: datetime
    
class AuthLogin(BaseModel):
    email: EmailStr
    password: str
    
class AuthResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"