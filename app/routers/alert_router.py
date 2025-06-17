from app import APIRouter


alert = APIRouter()


@alert.get("/")
async def running():
    return {"message":"alert is running"}