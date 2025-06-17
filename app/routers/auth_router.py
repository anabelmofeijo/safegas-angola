from app import APIRouter


auth = APIRouter()

@auth.get("/")
async def running():
    return {"message":"Auth is running"}