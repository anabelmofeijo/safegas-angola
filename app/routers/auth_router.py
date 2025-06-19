from app import APIRouter
from app.schemas.auth_schema import AuthRegister, AuthLogin
from app.services.auth_service import (
    AuthDatabase,
    AuthService
)


router = APIRouter()

@router.get("/")
async def running():
    return {"message":"Auth is running"}

@router.get("/list/")
async def list_user():
    service = AuthService()
    response = service.AuthListUsers()
    return response

@router.post("/post/")
async def create_user(data: AuthRegister):
    service = AuthDatabase()
    response = service.AuthAdd(data.dict())
    return response

@router.post("/login/")
async def login(data: AuthLogin):
    service = AuthService()
    response = service.AuthLogIn(data)
    return response

@router.delete("/delete/{id}")
async def delete_user(id: int):
    service = AuthDatabase()
    response = service.AuthDelete(id=id)
    return response