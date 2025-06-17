from app import  APIRouter

control = APIRouter()

@control.get("/")
async def running():
    return {"message":"Control is running"}