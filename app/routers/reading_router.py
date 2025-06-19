from app import APIRouter
from app.services.reading_service import ReadingService
from app.schemas.reading_schema import ReadingCreate

router = APIRouter()

@router.get("/")
async def running():
    return {"message":"Reading is running"}

@router.post("/post/")
async def add_reading(data: ReadingCreate):
    service = ReadingService()
    response = service.ReadingAdd(data.dict())
    return response

@router.get("/list/")
async def reading_list():
    service = ReadingService()
    response = service.ReadingList()
    return response

@router.get("/{id}")
async def find(id: int):
    service = ReadingService()
    response = service.ReadingById(id=id)
    return response

@router.get("/user/{id}")
async def reading_user_by_id(id: int):
    service = ReadingService()
    response = service.ReadingUserById(user_id=id)
    return response

@router.delete("/delete/{id}")
async def delete_reading(id: int):
    service = ReadingService()
    response = service.DeleteReading(id)
    return response 