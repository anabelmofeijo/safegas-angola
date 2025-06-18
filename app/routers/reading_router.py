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

@reading.get("/list/")
async def reading_list():
    service = ReadingService()
    response = service.ReadingList()
    return response

@reading.get("/{id}")
async def find(id: int):
    service = ReadingService()
    response = service.ReadingById(id=id)
    return response

@reading.get("/user/{id}")
async def reading_user_by_id(id: int):
    service = ReadingService()
    response = service.ReadingUserById(user_id=id)
    return response