from app import BaseModel, datetime
from app import EmailStr


class AuthRegister(BaseModel):
    name: str
    email: EmailStr
    password: str 
    
class AuthLogin(BaseModel):
    email: EmailStr
    password: str