from app import APIRouter
from app.services.reading_service import ReadingService
from app.schemas.reading_schema import (
    ReadingCreate,
    ReadingResponse
)

reading = APIRouter()

@reading.get("/")
async def running():
    return {"message":"Reading is running"}

@reading.post("/post/")
async def add_reading(data: ReadingCreate):
    service = ReadingService()
    response = service.ReadingAdd(data)
    return response