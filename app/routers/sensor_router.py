from app import APIRouter


sensor = APIRouter()

@sensor.get("/")
async def running():
    return {"message":"sensor is running"}