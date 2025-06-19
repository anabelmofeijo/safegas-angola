from app import APIRouter
from app.services.sensor_service import SensorService
from app.schemas.sensor_schema import SensorRegister


router = APIRouter()

@router.get("/")
async def running():
    return {"message":"sensor is running"}

@router.post("/register/")
async def sensor_register(data: SensorRegister):
    service = SensorService()
    response = service.SensorAdd(data=data.dict())
    return response

@router.get("/list/")
async def list_sensor():
    service = SensorService()
    response = service.SensorListAll()
    return response

@router.get("/find/{sensor_name}")
async def find_sensor(sensor_name: str):
    service = SensorService()
    response = service.FindSensor(sensor_name)
    return response

@router.delete("/delete/{id}")
async def delete_sensor(id: int):
    service = SensorService()
    response = service.SensorDelete(id)
    return response