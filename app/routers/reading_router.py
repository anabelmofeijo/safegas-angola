from app import APIRouter

reading = APIRouter()

@reading.get("/")
async def running():
    return {"message":"Reading is running"}